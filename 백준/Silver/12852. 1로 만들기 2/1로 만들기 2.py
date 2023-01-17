import sys
from collections import deque

n = int(sys.stdin.readline())
dp = deque()
dp.append([n])

result = []

while dp :
    a = dp.popleft()
    b = a[0]
    
    if b == 1 :
        result = a
        break
        
    if b % 3 == 0 :
        dp.append([b // 3] + a)
        
    if b % 2 == 0 :
        dp.append([b // 2] + a)
        
    dp.append([b - 1] + a)
    
print(len(result) - 1)
print(*result[::-1])