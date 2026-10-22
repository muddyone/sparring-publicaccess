from itertools import combinations
from functools import lru_cache
O=range(6); P=list(combinations(O,2))
T=[frozenset(s) for k in range(1,7) for s in combinations(O,k)]
def lit(p,r,t):
    n=len(set(p)&t)
    return {'or':n>=1,'and':n==2,'xor':n==1}[r]
def run(rules,k=4):
    H=[(p,r) for p in P for r in rules]
    L={(i,t):lit(*H[i],t) for i in range(len(H)) for t in T}
    @lru_cache(None)
    def v(S,k):
        if len(S)<=1: return 1.0
        if k==0:
            # must name pair and rule: score = max mass of single hypothesis
            return 1/len(S)
        b=0
        for t in T:
            y=frozenset(i for i in S if L[(i,t)]); n=S-y
            if not y or not n: continue
            b=max(b,(len(y)*v(y,k-1)+len(n)*v(n,k-1))/len(S))
        return b or 1/len(S)
    return v(frozenset(range(len(H))),k)
print('or/and', run(('or','and')))
print('or/and/xor', run(('or','and','xor')))
