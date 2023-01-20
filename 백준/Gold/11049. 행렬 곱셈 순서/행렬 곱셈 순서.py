import sys

n = int(sys.stdin.readline())
number = [list(map(int, sys.stdin.readline().split())) for i in range(n)]

dp = [[0] * n for i in range(n)]

for i in range(n-1):
    dp[i][i+1] = number[i][0] * number[i+1][0] * number[i+1][1]

for i in range(2, n) :
    for j in range(n - i) :
        dp[j][j+i] = 2**32
        for k in range(j, j+i) : 
            dp[j][j+i] = min(dp[j][j+i], 
                             dp[j][k] + dp[k+1][j+i] + number[j][0] * number[k][1] * number[j+i][1])

print(dp[0][-1])