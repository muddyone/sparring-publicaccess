#!/usr/bin/env python3
"""Multi-turn chat for the four vendors, with the sampling settings the design pins (§4).

Why not Rapier's client: it is single-turn (one system + one prompt), passes no temperature or
reasoning setting, and returns no token counts. This study needs a conversation per machine
(test, result, next test), pinned settings, and usage in every log line.

SETTINGS ARE REQUESTED, AND WHAT WAS SENT IS RECORDED. Each model has a settings dict
(temperature, seed, reasoning effort). Some models reject some of them (reasoning models often
refuse temperature). When a vendor returns a 400 naming a parameter, that parameter is dropped,
the call is retried once without it, and the drop is returned with the response so the call log
shows exactly what the model ran under. A silent drop would be an unrecorded change of
condition; this makes it a recorded one.

Keys come from the environment only (source the project .env first). Nothing here prints a key.
"""
from __future__ import annotations

import json
import os
import re
import time
from dataclasses import dataclass, field

import requests

ENDPOINTS = {
    "anthropic": ("https://api.anthropic.com/v1/messages", "ANTHROPIC_API_KEY"),
    "openai": ("https://api.openai.com/v1/chat/completions", "OPENAI_API_KEY"),
    "gemini": ("https://generativelanguage.googleapis.com/v1beta/openai/chat/completions", "GEMINI_API_KEY"),
    "xai": ("https://api.x.ai/v1/chat/completions", "XAI_API_KEY"),
}

# Settings a vendor may refuse, in the order they are dropped if a 400 names none of them.
_DROPPABLE = ("temperature", "seed", "reasoning_effort", "thinking", "top_p")


@dataclass
class Reply:
    text: str
    usage: dict
    finish: str
    sent: dict                      # the settings actually sent on the successful call
    dropped: list = field(default_factory=list)
    latency_s: float = 0.0


class ChatError(RuntimeError):
    pass


def _post(url: str, headers: dict, payload: dict, timeout: int = 180) -> requests.Response:
    delay = 2.0
    last = None
    for _ in range(6):
        try:
            r = requests.post(url, headers=headers, json=payload, timeout=timeout)
        except requests.RequestException as exc:
            last = type(exc).__name__
            time.sleep(delay)
            delay = min(delay * 2, 60)
            continue
        if r.status_code == 429 or r.status_code >= 500:
            ra = r.headers.get("Retry-After", "")
            wait = float(ra) if ra.replace(".", "", 1).isdigit() else delay
            last = f"HTTP {r.status_code}"
            time.sleep(min(wait, 60))
            delay = min(delay * 2, 60)
            continue
        return r
    raise ChatError(f"{url}: failed after retries ({last})")


def _payload(vendor: str, model: str, system: str, messages: list[dict], settings: dict,
             max_tokens: int) -> dict:
    if vendor == "anthropic":
        # Prompt caching: mark the last message, so the conversation so far is cached and the next
        # turn reads it back at the cache rate. Changes the bill, not what the model sees. The
        # other three vendors cache automatically.
        *head, last = messages
        last = {"role": last["role"],
                "content": [{"type": "text", "text": last["content"], "cache_control": {"type": "ephemeral"}}]}
        p = {"model": model, "max_tokens": max_tokens, "system": system, "messages": [*head, last]}
        if settings.get("temperature") is not None:
            p["temperature"] = settings["temperature"]
        if settings.get("thinking"):
            p["thinking"] = settings["thinking"]
        return p
    p = {"model": model, "messages": [{"role": "system", "content": system}, *messages]}
    p["max_completion_tokens" if vendor == "openai" else "max_tokens"] = max_tokens
    for k in ("temperature", "seed", "reasoning_effort", "top_p"):
        if settings.get(k) is not None:
            p[k] = settings[k]
    return p


def _parse(vendor: str, data: dict) -> tuple[str, dict, str]:
    if vendor == "anthropic":
        text = "".join(b.get("text", "") for b in data.get("content", []) if b.get("type") == "text")
        return text, data.get("usage", {}), data.get("stop_reason", "")
    ch = (data.get("choices") or [{}])[0]
    return (ch.get("message", {}) or {}).get("content") or "", data.get("usage", {}), ch.get("finish_reason", "")


def chat(vendor: str, model: str, system: str, messages: list[dict], settings: dict,
         max_tokens: int = 2000) -> Reply:
    url, key_env = ENDPOINTS[vendor]
    key = os.environ.get(key_env)
    if not key:
        raise ChatError(f"{key_env} is not set")
    if vendor == "anthropic":
        headers = {"x-api-key": key, "anthropic-version": "2023-06-01", "content-type": "application/json"}
    else:
        headers = {"Authorization": f"Bearer {key}", "Content-Type": "application/json"}

    settings = dict(settings)
    dropped: list[str] = []
    for _ in range(len(_DROPPABLE) + 1):
        t0 = time.time()
        r = _post(url, headers, _payload(vendor, model, system, messages, settings, max_tokens))
        if r.status_code == 200:
            text, usage, finish = _parse(vendor, r.json())
            return Reply(text=text, usage=usage, finish=finish, sent=settings, dropped=dropped,
                         latency_s=round(time.time() - t0, 2))
        body = r.text[:600]
        if r.status_code == 400:
            named = [k for k in _DROPPABLE if k in settings and re.search(k.split("_")[0], body, re.I)]
            if named:
                for k in named:
                    settings.pop(k, None)
                    dropped.append(k)
                continue
        raise ChatError(f"{vendor}/{model}: HTTP {r.status_code}: {body}")
    raise ChatError(f"{vendor}/{model}: settings could not be satisfied (dropped {dropped})")


if __name__ == "__main__":  # smoke test: one short call per configured model
    import sys
    cfg = json.loads(open(sys.argv[1]).read())
    for name, m in cfg["models"].items():
        try:
            rep = chat(m["vendor"], m["model"], "Reply with one word.", [{"role": "user", "content": "Say ready."}],
                       m.get("settings", {}), max_tokens=m.get("max_tokens", 2000))
            print(f"{name:<10} ok  {rep.text.strip()[:30]!r}  finish={rep.finish}  dropped={rep.dropped}  usage={rep.usage}")
        except ChatError as exc:
            print(f"{name:<10} ERROR {exc}"[:400])
