import sys


n = int(sys.stdin.readline())
    
dp = [1, 1, 1]

for i in range(3, 101) :
    dp.append(dp[i-3] + dp[i-2])


for i in range(n) :
    
    k = int(sys.stdin.readline())
    
    print(dp[k-1])
    