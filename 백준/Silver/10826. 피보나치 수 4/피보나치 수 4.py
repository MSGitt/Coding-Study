import sys 

n = int(sys.stdin.readline())
a = 0 
b = 1 

if n < 2 : 
    print(n) 
    
else : 
    for i in range(2, n+1) :
        a , b = b , a + b 
    
    print(b)