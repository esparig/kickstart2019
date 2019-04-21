from collections import defaultdict as ddic, deque
from itertools import combinations, permutations, product
import sys
sys.setrecursionlimit(10**6)
stdout = sys.stdout
rr = lambda: raw_input().strip()
rri = lambda: int(raw_input())
rrm = lambda: list(map(int, raw_input().strip().split()))

def solve(N, Q, A, queries):
    P = [[0] * 26]
    for x in A:
        count = P[-1][:]
        count[x] ^= 1
        P.append(count)
    #for row in P:
    #    print row
    ans = 0
    for L, R in queries:
        # L, R in 1 indexed
        L -= 1
        R -= 1
        row1 = P[L]
        row2 = P[R+1]
        parity = (R%2) ^ (L%2) ^ 1
        ct = 0
        for i in xrange(26):
            ct += row1[i] ^ row2[i]
        if ct == parity:
            ans += 1
        
        #print('LR', L, R, parity, ct, row1, row2)
    return ans

    
###
T = rri()
for tc in xrange(1, T+1):
    N, Q = rrm()
    A = [ord(c) - ord('A') for c in rr()]
    queries = [rrm() for _ in xrange(Q)]
    ans = solve(N, Q, A, queries)
    print("Case #{}: {}".format(tc, ans))
    
