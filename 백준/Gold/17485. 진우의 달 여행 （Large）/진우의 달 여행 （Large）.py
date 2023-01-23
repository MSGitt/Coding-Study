import sys

n, m = map(int, sys.stdin.readline().split())

matrix = [list(map(int, sys.stdin.readline().split())) for i in range(n)]

dp = [[[float('inf')] * 3 for i in range(m)] for i in range(n)]

for i in range(n) :
    if i == 0 :
        for j in range(m) :
            for d in range(3) :
                dp[i][j][d] = matrix[i][j]
                
    else :
        for l in range(m) :
            if l == 0 :
                dp[i][l][1] = min(dp[i-1][l][0], dp[i-1][l][2]) + matrix[i][l]
                dp[i][l][2] = min(dp[i-1][l+1][0], dp[i-1][l+1][1]) + matrix[i][l]
                
            elif l == m - 1 :
                dp[i][l][0] = min(dp[i-1][l-1][1], dp[i-1][l-1][2]) + matrix[i][l]
                dp[i][l][1] = min(dp[i-1][l][0], dp[i-1][l][2]) + matrix[i][l]
                
            else :
                dp[i][l][0] = min(dp[i-1][l-1][1], dp[i-1][l-1][2]) + matrix[i][l]
                dp[i][l][1] = min(dp[i-1][l][0], dp[i-1][l][2]) + matrix[i][l]
                dp[i][l][2] = min(dp[i-1][l+1][0], dp[i-1][l+1][1]) + matrix[i][l]
                
res = float('inf')

for i in range(m) :
    res = min(res, min(dp[-1][i]))

print(res)