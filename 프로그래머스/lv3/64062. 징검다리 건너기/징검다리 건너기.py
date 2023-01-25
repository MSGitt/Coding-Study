def solution(stones, k):
    
    left, right = min(stones), max(stones)
    
    while left <= right :    
        mid = (left + right) // 2
        count = 0 
        
        for i in stones :
            if i - mid <= 0 :
                count += 1 
                if count >= k :
                    right = mid - 1
                    break
                    
            else : 
                count = 0
                
        else :
            left = mid + 1
        
    
    return left