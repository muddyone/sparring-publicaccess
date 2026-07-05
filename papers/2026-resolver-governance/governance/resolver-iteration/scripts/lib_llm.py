"""Minimal dual-vendor LLM client for the resolver-iteration study.

Claude via /v1/messages, GPT via /v1/chat/completions. Tolerant JSON extraction,
retry with backoff, thread-safe. Keys come from the project .env (loaded by caller
into the environment).

Model ids are pinned in run_study.py; this module is vendor-mechanics only.
"""
import os, re, json, time, threading, requests

CLAUDE_URL = "https://api.anthropic.com/v1/messages"
OPENAI_URL = "https://api.openai.com/v1/chat/completions"

# Serialize nothing globally; requests is thread-safe per-call. We do bound a
# polite call rate per vendor to avoid 429 storms.
_rate_lock = threading.Lock()
_last_call = {"claude": 0.0, "gpt": 0.0}
_MIN_GAP = {"claude": 0.05, "gpt": 0.05}


def _throttle(vendor):
    with _rate_lock:
        now = time.monotonic()
        gap = _MIN_GAP[vendor]
        wait = _last_call[vendor] + gap - now
        if wait > 0:
            time.sleep(wait)
        _last_call[vendor] = time.monotonic()


class LLMError(RuntimeError):
    pass


def _retry(fn, what, tries=6):
    delay = 4.0
    last = None
    for i in range(tries):
        try:
            return fn()
        except Exception as e:  # noqa: BLE001 - we want to retry broadly
            last = e
            msg = str(e)
            # Don't retry obvious client errors except rate limits / overload.
            if any(s in msg for s in ("status 400", "status 401", "status 403", "status 404")):
                raise
            time.sleep(delay)
            delay = min(delay * 1.8, 60.0)
    raise LLMError(f"{what}: exhausted retries: {last}")


def call_claude(model, system, user, max_tokens=4000, temperature=None):
    # temperature is accepted for signature compatibility but NOT sent:
    # claude-opus-4-8 rejects the parameter ("deprecated for this model").
    def _do():
        _throttle("claude")
        r = requests.post(
            CLAUDE_URL,
            headers={
                "x-api-key": os.environ["ANTHROPIC_API_KEY"],
                "anthropic-version": "2023-06-01",
                "content-type": "application/json",
            },
            json={
                "model": model,
                "max_tokens": max_tokens,
                "system": system,
                "messages": [{"role": "user", "content": user}],
            },
            timeout=300,
        )
        if r.status_code != 200:
            raise LLMError(f"claude status {r.status_code}: {r.text[:300]}")
        d = r.json()
        parts = [b.get("text", "") for b in d.get("content", []) if b.get("type") == "text"]
        return "".join(parts)

    return _retry(_do, f"claude({model})")


def call_gpt(model, system, user, max_completion_tokens=16000):
    def _do():
        _throttle("gpt")
        r = requests.post(
            OPENAI_URL,
            headers={
                "Authorization": f"Bearer {os.environ['OPENAI_API_KEY']}",
                "Content-Type": "application/json",
            },
            json={
                "model": model,
                "messages": [
                    {"role": "system", "content": system},
                    {"role": "user", "content": user},
                ],
                "max_completion_tokens": max_completion_tokens,
                "response_format": {"type": "json_object"},
            },
            timeout=300,
        )
        if r.status_code != 200:
            raise LLMError(f"gpt status {r.status_code}: {r.text[:300]}")
        d = r.json()
        return d["choices"][0]["message"]["content"] or ""

    return _retry(_do, f"gpt({model})")


def extract_json(text):
    """Tolerant: strip code fences, grab the outermost {...} or [...]."""
    if text is None:
        raise LLMError("empty text for json extraction")
    t = text.strip()
    t = re.sub(r"^```(?:json)?\s*", "", t)
    t = re.sub(r"\s*```$", "", t)
    try:
        return json.loads(t)
    except Exception:
        pass
    # Find first balanced object/array.
    for opener, closer in (("{", "}"), ("[", "]")):
        start = t.find(opener)
        if start == -1:
            continue
        depth = 0
        for i in range(start, len(t)):
            c = t[i]
            if c == opener:
                depth += 1
            elif c == closer:
                depth -= 1
                if depth == 0:
                    try:
                        return json.loads(t[start : i + 1])
                    except Exception:
                        break
    raise LLMError(f"could not extract JSON from: {text[:200]}")


def claude_json(model, system, user, max_tokens=4000, temperature=0.7):
    sys2 = system + "\n\nRespond with STRICT JSON only — no prose, no markdown fences."
    return extract_json(call_claude(model, sys2, user, max_tokens, temperature))


def gpt_json(model, system, user, max_completion_tokens=16000):
    sys2 = system + "\n\nRespond with STRICT JSON only."
    return extract_json(call_gpt(model, sys2, user, max_completion_tokens))
