import sys
from collections import defaultdict
import copy

n, m, h = map(int, sys.stdin.readline().split())

dp = [[0] * (h + 1) for i in range(n + 1)]
dp[0][0] = 1

for i in range(1, n + 1) :
    
    dp[i] = dp[i-1].copy()
    numbers = list(map(int, sys.stdin.readline().split()))
    
    for j in numbers :
        for k in range(j, h + 1) :
            dp[i][k] += dp[i-1][k-j]
            
print(dp[-1][-1] % 10007)