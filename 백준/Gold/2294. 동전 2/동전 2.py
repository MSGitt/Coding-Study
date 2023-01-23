import sys

n, k = map(int, sys.stdin.readline().split())

coin = [int(sys.stdin.readline()) for i in range(n)]
dp = [float('inf')] * (k + 1)

dp[0] = 0

for i in coin :
    for j in range(i, k + 1) :
        dp[j] = min(dp[j - i] + 1, dp[j])
        
if dp[-1] == float('inf') :
    print(-1)  

else :    
    print(dp[-1])