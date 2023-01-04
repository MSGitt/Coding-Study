import sys

n = int(sys.stdin.readline())

triangle = [list(map(int, sys.stdin.readline().split())) for i in range(n)]
dp = [[0]* (i+1) for i in range(n)]

for i in range(n) :
    dp[-1][i] = triangle[-1][i]


for i in reversed(range(n-1)) :
    for j in range(i+1) :
        dp[i][j] = triangle[i][j] + max(dp[i+1][j], dp[i+1][j+1])
        

print(dp[0][0])