import sys

n = int(sys.stdin.readline())

number = [0] * (n + 1)
dp = [0] * (n + 1)

for i in range(1, n) :
    
    a, b = map(int, sys.stdin.readline().split())
    number[i] = (a, b)
    
k = int(sys.stdin.readline())   

if n > 1 :
    dp[2] = dp[1] + number[1][0] 

for i in range(3, n + 1) :   
    
    dp[i] = min(dp[i-1] + number[i-1][0], dp[i-2] + number[i-2][1])
    
result = dp[-1]

for i in range(1, n - 2) :
    
    dp1 = dp[:]
    dp1[i + 3] = dp1[i] + k
    
    for j in range(i + 4, n + 1) :
        
        dp1[j] = min(dp1[j-1] + number[j-1][0], dp1[j-2] + number[j-2][1])
        
    result = min(result, dp1[-1])
    
print(result)