import sys

n, k = map(int, sys.stdin.readline().split())

number = []
dp = [[0] * (k + 1) for i in range(n + 1)]

for i in range(n) :
    
    a, b = map(int, sys.stdin.readline().split())
    number.append((a, b))
    
for i in range(1, n + 1) :
    for j in range(1, k + 1) :
    
        weight, value = number[i - 1]

        if j < weight : 
            dp[i][j] = dp[i-1][j]

        else :
            dp[i][j] = max(dp[i-1][j-weight] + value, dp[i-1][j])
            
print(dp[-1][-1])