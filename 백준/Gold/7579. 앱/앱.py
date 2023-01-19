import sys

n, m = map(int, sys.stdin.readline().split())
memory = list(map(int, sys.stdin.readline().split()))
cost = list(map(int, sys.stdin.readline().split()))

k = sum(cost)
dp = [[0] * (n + 1) for i in range(k + 1)]

for i in range(1, k + 1) :
    for j in range(1, n + 1) :
        if i >= cost[j - 1] :
            dp[i][j] = max(dp[i][j-1], dp[i-cost[j-1]][j-1] + memory[j-1])
            
        else :
            dp[i][j] = dp[i][j-1]
            
    if max(dp[i]) >= m :
        print(i)
        break