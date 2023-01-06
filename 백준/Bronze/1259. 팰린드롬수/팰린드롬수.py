import sys

while True : 
    
    a = list(map(int, sys.stdin.readline().rstrip()))
    
    if a[0] == 0 :
        break
    
    if a == a[::-1] : 
        print('yes')
        
    else :
        print('no')