import sys 


t = int(sys.stdin.readline()) 


for i in range(t) : 
    
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())  
    n = int(sys.stdin.readline()) 
    count = 0
    
    for i in range(n) :
        cx, cy, r = map(int, sys.stdin.readline().split()) 
        d1 = (x1-cx)**2 + (y1-cy)**2 
        d2 = (x2-cx)**2 + (y2-cy)**2 
        
        if r**2 > d1 and r**2 > d2 :
            pass 
            
        elif r**2 > d2 :
            count += 1 
            
        elif r**2 > d1  :
            count += 1 
            
                   
    print(count)