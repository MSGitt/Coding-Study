import sys

n = int(sys.stdin.readline())

number = [0] * (n + 1)
dp = [0] * (n + 1)

for i in range(1, n + 1) :
    
    a, b = map(int, sys.stdin.readline().split())
    number[i] = (a, b)
    
for i in range(1, n + 1) :
    
    dp[i] = max(dp[i], dp[i - 1])
    finish = i + number[i][0] - 1
    
    if finish <= n :
        dp[finish] = max(dp[finish], dp[i - 1] + number[i][1])
        
print(max(dp))