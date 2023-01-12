def solution(priorities, location):
    
    queue = [(i, p) for i, p in enumerate(priorities)]
    
    m = max(priorities) 
    result = 0
    
    while True :
        k = queue.pop(0)
        
        if k[1] != max(priorities) :
            queue.append(k)
            
        else : 
            result += 1 
            priorities.remove(k[1])
            
            if k[0] == location :
                return result