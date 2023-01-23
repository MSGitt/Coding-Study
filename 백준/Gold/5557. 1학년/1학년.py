import sys 

n = int(sys.stdin.readline())

number = list(map(int, sys.stdin.readline().split()))
dp = [[0] * 21 for i in range(n - 1)]

dp[0][number[0]] = 1

for i in range(1, n-1) :
    for j in range(21) :
        if j - number[i] >= 0 :
            dp[i][j-number[i]] += dp[i-1][j]
            
        if j + number[i] <= 20 :
            dp[i][j+number[i]] += dp[i-1][j]
            
print(dp[-1][number[-1]])    