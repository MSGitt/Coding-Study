import sys


n = int(sys.stdin.readline())

number = list(map(int, sys.stdin.readline().split()))
dp = [0] * n
max_num = number[0]

for i in range(n) :
    for j in range(n) :
        if number[i] > number[j] and dp[i] < dp[j] :
            dp[i] = dp[j]

    dp[i] += 1
        
print(max(dp))

    
    
        
