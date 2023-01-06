import sys


while True :
    a = list(map(int, sys.stdin.readline().split())) 
    
    if sum(a) == 0 :
        break 
        
    a.sort()
    
    if a[2]**2 == a[0]**2 + a[1]**2 :
        print('right')
        
    else :
        print('wrong')