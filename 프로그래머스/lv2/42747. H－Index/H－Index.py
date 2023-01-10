def solution(citations):
    
    citations.sort()
    
    n = len(citations)
    result = 0
    
    for i in range(n) :
        h = citations[i]
        k = n - i
        
        result = max(result, min(h, k))
    
    return result 
    