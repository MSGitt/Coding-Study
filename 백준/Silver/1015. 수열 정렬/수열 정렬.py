import sys 


n = int(sys.stdin.readline()) 
a = list(map(int, sys.stdin.readline().split())) 

result = [i for i in range(n)]
idx = 0 

for i in range(n) : 
    min_idx = a.index(min(a)) 
    a[min_idx] = 2000 
    result[min_idx] = idx 
    idx += 1 
    
print(*result)
    