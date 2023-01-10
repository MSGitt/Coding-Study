def solution(sizes):
    
    r1 = 0
    r2 = 0
    
    for i in sizes :
        n1 = max(i)
        n2 = min(i) 
        
        r1 = max(r1, n1)
        r2 = max(r2, n2)
        
    return r1 * r2