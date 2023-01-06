import sys


n, m = map(int, sys.stdin.readline().split())
a = m

result1 = 1 
result2 = 1
i = 0

while i < a :
    
    result1 *= n
    result2 *= m 
    
    n -= 1
    m -= 1 
    
    i += 1
    
print(result1//result2)
    