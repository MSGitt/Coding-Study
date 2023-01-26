import sys

n, m = map(int, sys.stdin.readline().split())
number = []
number.sort()

for i in range(n) :
    number.append(int(sys.stdin.readline()))
    
left, right = 0, max(number) * m

ans = float('inf')

while left <= right :
    
    total = 0
    mid = (left + right) // 2
    
    for i in number :
        total += mid // i
        
    if total >= m :
        right = mid - 1
        ans = min(ans, mid)
        
    else :
        left = mid + 1
                
print(ans)