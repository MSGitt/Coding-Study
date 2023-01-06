import sys 


w, h, x, y, p = map(int, sys.stdin.readline().split()) 

coord = []
result = 0

for i in range(p) :
    a, b = map(int, sys.stdin.readline().split()) 
    coord.append((a, b)) 
    
for j in coord :
    if j[0] >= x and j[0] <= x + w and j[1] >= y and j[1] <= y + h :
        result += 1 
        
        
    elif j[0] < x :
        if (x-j[0])**2 + (abs(j[1] - (y + 0.5*h)))**2 <= (0.5*h)**2 :
            result += 1 
        
    elif j[0] > x + w :
        if (j[0] - (x + w))**2 + (abs(j[1]- (y+0.5*h)))**2 <= (0.5*h)**2 :
            result += 1 
            
print(result)