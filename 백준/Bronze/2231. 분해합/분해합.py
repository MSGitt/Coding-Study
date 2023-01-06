import sys

n = int(sys.stdin.readline())

result = 0

for i in range(1, n+1) :
    k = list(map(int, str(i)))
    result = i + sum(k) 
    
    if result == n :
        print(i)
        break
        
    if i == n :
        print(0)
        
    result = 0