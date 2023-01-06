import sys 

k = int(sys.stdin.readline()) 

a = 1 
b = 0

for i in range(k) : 
    c = a 
    d = b 
    
    b = c + d 
    a = d 
    
print(a, b)
    
    
    
    
    