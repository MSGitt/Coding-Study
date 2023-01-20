import sys

x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
x3, y3, x4, y4 = map(int, sys.stdin.readline().split())

def ccw(x1, y1, x2, y2, x3, y3) :
    
    temp = (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)
    
    if temp > 0 :
        return 1
    
    elif temp == 0 :
        return 0
    
    else :
        return -1
    
temp1 = ccw(x1, y1, x2, y2, x3, y3)
temp2 = ccw(x1, y1, x2, y2, x4, y4)

temp3 = ccw(x3, y3, x4, y4, x1, y1)
temp4 = ccw(x3, y3, x4, y4, x2, y2) 

if temp1 * temp2 == 0 and temp3 * temp4 == 0 :
    if (min(x3, x4) <= max(x1, x2) and min(y3, y4) <= max(y1, y2)) and (min(x1, x2) <= max(x3, x4) and min(y1, y2) <= max(y3, y4)) :
        print(1)
        sys.exit()

else :
    if temp1 * temp2 <= 0 and temp3 * temp4 <= 0 :
        print(1)
        sys.exit()
        
print(0)