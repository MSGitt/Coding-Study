import heapq

def solution(jobs):
    
    result, now, i = 0, 0, 0
    
    start = -1
    temp = []
    
    while i < len(jobs) :
        
        for j in jobs :
            if start < j[0] <= now :
                heapq.heappush(temp, (j[1], j[0]))
            
        if len(temp) > 0 :
            k = heapq.heappop(temp)
            start = now 
            now += k[0]
            
            result += now - k[1]
            i += 1
            
        else : 
            now += 1         
            
    return result // len(jobs)