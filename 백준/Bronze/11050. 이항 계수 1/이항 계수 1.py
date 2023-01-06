import sys


a, b = map(int, sys.stdin.readline().split())

result = 1
div = 1

for i in range(b) : 
    
    result *= a 
    a -= 1 
    
    div *= b 
    b -= 1 
    
    
print(result//div)