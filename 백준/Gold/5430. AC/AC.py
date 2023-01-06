import sys
from collections import deque


n = int(sys.stdin.readline())

for i in range(n) :
    
    order = sys.stdin.readline().rstrip()
    m = int(sys.stdin.readline())
    
    number = deque(sys.stdin.readline().rstrip()[1:-1].split(','))
    
    if m == 0 :
        number = []
    
    flag = 1
    count = 0
    
    for j in range(len(order)) :
        
        if order[j] == 'R' :
            count += 1
            
        elif order[j] == 'D' :
            if not number :
                print("error")
                flag = 0
                break
            
            else :
                if count % 2 == 0:
                    number.popleft()
                
                else :
                    number.pop()
                        
    if flag == 1 :
        if count % 2 == 0 :
            print('['+','.join(number)+']')
        
        else : 
            number.reverse()
            print('['+','.join(number)+']')