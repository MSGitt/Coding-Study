import sys
from bisect import bisect_left

n = int(sys.stdin.readline())
number = list(map(int, sys.stdin.readline().split()))

result = []
ans = 0

for i in number :
    if not result:
        result.append(i)
        ans += 1
        continue
        
    if result[-1] < i :
        result.append(i)
        ans += 1
        
    else :
        idx = bisect_left(result, i)
        result[idx] = i
        
print(ans)