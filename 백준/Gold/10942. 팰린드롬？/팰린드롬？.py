import sys

n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())

dp = [[0] * n for i in range(n)]

for i in range(n) :
    dp[i][i] = 1
    
for i in range(n - 1) :
    if num[i] == num[i+1] :
        dp[i][i+1] = 1
        
for i in range(2, n) :
    for j in range(n - i) :
        if num[j] == num[i+j] and dp[j+1][i+j-1] == 1:
            dp[j][j+i] = 1
            
for i in range(m) :
    
    a, b = map(int, sys.stdin.readline().split())
    print(dp[a-1][b-1])