import sys 


t = int(sys.stdin.readline()) 

for i in range(t) : 
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split()) 
    distance = ((x2 - x1)**2 + (y2 - y1)**2)**(0.5) 
    
    if distance == 0 and  r1 == r2 :
        print(-1)
    
    elif abs(r1-r2) < distance < r1 + r2 :
        print(2) 
        
    elif distance == abs(r1 - r2) or distance == r1 + r2 : 
        print(1) 
        
    else : 
        print(0) 