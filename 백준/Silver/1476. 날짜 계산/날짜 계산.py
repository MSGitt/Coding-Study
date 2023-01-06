import sys 

a, b, c = map(int, sys.stdin.readline().split()) 

i = 0
e = 0 
s = 0
m = 0 

while True : 
   
    if e == 16 : 
        e = 1 
    if s == 29 :
        s = 1 
    if m == 20 : 
        m = 1 
    
    if e == a and s == b and m == c : 
        break 
        
    e += 1 
    s += 1 
    m += 1 
    i += 1 
    
       
    
print(i)
   
        