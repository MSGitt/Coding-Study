import sys


n = int(sys.stdin.readline())


for i in range(n) :
    
    m, n = map(int, sys.stdin.readline().split())
    queue = list(map(int, sys.stdin.readline().split()))
    
    count = 0
    
    while True :
        
        if queue[0] == max(queue) :
            count += 1 
            n -= 1
            del queue[0] 
            
            
        else :
            queue.append(queue[0])
            del queue[0]
            
            if n == 0 :
                n = len(queue) - 1
                
            else :
                n -= 1 
                
        if n == -1 :
            break
            
    print(count)
                
           
            
        
    