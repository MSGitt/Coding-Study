import sys

s1 = sys.stdin.readline().rstrip()
s2 = sys.stdin.readline().rstrip()

result1 = []
result2 = []

n1 = len(s1)
n2 = len(s2)
dp = [[""] * (n2 + 1) for i in range(n1 + 1)]

for i in range(1, n1 + 1) :
    for j in range(1, n2 + 1) :
        if s1[i-1] == s2[j-1] :
            dp[i][j] = dp[i-1][j-1] + s1[i-1]
            
        else :
            if len(dp[i-1][j]) > len(dp[i][j-1]) :
                dp[i][j] = dp[i-1][j]
            else :
                dp[i][j] = dp[i][j-1]
        
print(len(dp[-1][-1]))
print(dp[-1][-1])