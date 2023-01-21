import sys
from bisect import bisect_left

n = int(sys.stdin.readline())
number = [0] + list(map(int, sys.stdin.readline().split()))

dp = [0] * (n + 1)
result = [-float('inf')]

for i in range(1, n + 1) :
    if number[i] > result[-1] :
        result.append(number[i])
        dp[i] = len(result) - 1
        
    else :
        idx = bisect_left(result, number[i])
        dp[i] = idx
        result[idx] = number[i]
        
print(len(result) - 1)

max_idx = max(dp)
ans = []

for i in reversed(range(n + 1)) :
    if dp[i] == max_idx :
        ans.append(number[i])
        max_idx -= 1

print(*ans[::-1][1:])