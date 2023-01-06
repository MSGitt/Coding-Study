import sys 


n, m, k = map(int, sys.stdin.readline().split()) 

count = 0

while m != k : 
    
    m -= m // 2 
    k -= k // 2 
    
    count += 1 
    
print(count)
    
    