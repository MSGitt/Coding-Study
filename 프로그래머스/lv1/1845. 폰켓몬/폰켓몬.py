def solution(nums):
   
    
    n = len(nums) // 2
    
    num = set(nums) 
    
    if len(num) > n :
        return n 
    
    return len(num)
