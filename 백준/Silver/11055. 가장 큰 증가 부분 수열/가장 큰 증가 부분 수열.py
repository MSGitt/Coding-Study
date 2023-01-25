import sys

n = int(sys.stdin.readline())
number = list(map(int, sys.stdin.readline().split()))

dp = number[:]

for i in range(1, n) :
    for j in range(i) :
        if number[i] > number[j] :
            dp[i] = max(dp[i], dp[j] + number[i])
    
print(max(dp))