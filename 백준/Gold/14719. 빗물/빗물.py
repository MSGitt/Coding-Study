import sys

h, w = map(int, sys.stdin.readline().split())

wall = list(map(int, sys.stdin.readline().split()))

result = 0

for i in range(1, w - 1) :
    
    left = max(wall[ :i])
    right = max(wall[i+1: ])
    
    m = min(left, right)
    
    if m > wall[i] :
        result += m - wall[i]
        
print(result)