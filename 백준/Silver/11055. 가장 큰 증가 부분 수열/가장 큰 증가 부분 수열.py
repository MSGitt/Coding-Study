import sys

n = int(sys.stdin.readline())
number = list(map(int, sys.stdin.readline().split()))

dp = [0] * n

for i in range(n) :
    for j in range(n) :
        if number[i] > number[j] and dp[i] < dp[j] :
            dp[i] = dp[j]
            
    dp[i] += number[i]
    
print(max(dp))