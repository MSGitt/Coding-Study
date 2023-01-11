from collections import deque
import math

def solution(progresses, speeds):
    
    queue = deque()
    for i in range(len(progresses)) :
        queue.append(math.ceil((100 - progresses[i]) / speeds[i]))
      
    temp, count = queue.popleft(), 1
    result = []

    while queue :
        
        a = queue.popleft()
        
        if a > temp :
            temp = a
            result.append(count)
            count = 1
            
        else :
            count += 1
            
    result.append(count)
                
    return result
