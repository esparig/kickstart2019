from collections import defaultdict as ddic, deque
from itertools import combinations, permutations, product
import sys
sys.setrecursionlimit(10**7)
stdout = sys.stdout
rr = lambda: raw_input().strip()
rri = lambda: int(raw_input())
rrm = lambda: list(map(int, raw_input().strip().split()))

def solve(N, stones):
    # stones[i] = S, E, L
    #  takes S seconds to eat
    #  contains E energy
    #  loses L units energy each second
    stones.sort(key = lambda (s,e,l): l / float(s), reverse = True)
    def energyat(i, t):
        return max(0, stones[i][1] - t * stones[i][2])
    
    memo = {}
    def dp(i, t):
        # on stones[i:] at time t, how much more energy can get?
        if i == N: return 0
        if (i, t) in memo: return memo[i, t]
        ans = dp(i+1, t)
        e_gain = energyat(i, t)
        if e_gain:
            ans = max(ans, dp(i+1, t + stones[i][0]) + e_gain)
        memo[i, t] = ans
        return ans

    return dp(0, 0)
    

    
###
T = rri()
for tc in xrange(1, T+1):
    N = rri()
    stones = [rrm() for _ in xrange(N)]
    ans = solve(N, stones)
    print("Case #{}: {}".format(tc, ans))
    
