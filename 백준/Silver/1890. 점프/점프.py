import sys
from collections import deque

n = int(sys.stdin.readline())

matrix = [list(map(int, sys.stdin.readline().split())) for i in range(n)]

row = [1, 0]
col = [0, 1]

dp = [[0] * n for i in range(n)]
dp[0][0] = 1

for i in range(n) :
    for j in range(n) :
        
        if i == n - 1 and j == n - 1 :
            print(dp[i][j])
            break
            
        if 0 <= j + matrix[i][j] < n :
            dp[i][j + matrix[i][j]] += dp[i][j]
            
        if 0 <= i + matrix[i][j] < n :
            dp[i + matrix[i][j]][j] += dp[i][j]