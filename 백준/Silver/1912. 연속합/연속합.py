import sys

n = int(sys.stdin.readline())
number = list(map(int, sys.stdin.readline().split()))

dp = [0] * n 
dp[0] = number[0]

for i in range(1, len(number)) : 
    dp[i] = max(number[i], dp[i - 1] + number[i])
    
print(max(dp))