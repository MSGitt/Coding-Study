import sys

n = int(sys.stdin.readline())

matrix = [list(map(int, sys.stdin.readline().split())) for i in range(n)]

dp = [[[0] * n for i in range(n)] for i in range(3)]
dp[0][0][1] = 1

for i in range(2, n) :
    if matrix[0][i] == 0 :
        dp[0][0][i] = dp[0][0][i - 1]
        
for i in range(1, n):
    for j in range(1, n):
        if matrix[i][j] == 0 and matrix[i][j-1] == 0 and matrix[i-1][j] == 0 :
            dp[2][i][j] = dp[0][i-1][j-1] + dp[1][i-1][j-1] + dp[2][i-1][j-1]
            
        if matrix[i][j] == 0 :
            dp[0][i][j] = dp[0][i][j-1] + dp[2][i][j-1]          
            dp[1][i][j] = dp[1][i-1][j] + dp[2][i-1][j]
            
print(dp[0][-1][-1] + dp[1][-1][-1] + dp[2][-1][-1])            