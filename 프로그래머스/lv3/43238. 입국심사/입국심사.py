def solution(n, times):
    
    left, right = 1, max(times) * n
    answer = 0
    
    while left <= right :
        
        count = 0
        mid = (left + right) // 2 
        
        for i in times :
            count += mid // i
            if count >= n :
                break
            
        if count >= n :
            answer = mid
            right = mid - 1
            
        else :
            left = mid + 1 
            
    return answer