import sys


n = int(sys.stdin.readline())

number = [list(map(int, sys.stdin.readline().split())) for i in range(n)]
dp = [[0] * 3 for i in range(n)]

dp[0][0] = number[0][0]
dp[0][1] = number[0][1]
dp[0][2] = number[0][2]

for i in range(1, n) :
    
    dp[i][0] = number[i][0] + min(dp[i-1][1], dp[i-1][2])
    dp[i][1] = number[i][1] + min(dp[i-1][0], dp[i-1][2])    
    dp[i][2] = number[i][2] + min(dp[i-1][0], dp[i-1][1])
    
    
print(min(dp[n-1]))