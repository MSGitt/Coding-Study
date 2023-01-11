from collections import deque

def dfs(x, n, target, numbers) : 
    
    stack = deque()
    stack.append((numbers[x], 0))
    stack.append((-numbers[x], 0))
    
    count = 0
            
    while stack :
        v, d = stack.pop()
        d += 1 
        
        if d == n :
            if v == target :
                count += 1 
                
        elif d < n : 
            stack.append((v + numbers[d], d))
            stack.append((v - numbers[d], d))
            
    return count

def solution(numbers, target):
    
    answer = dfs(0, len(numbers), target, numbers)   
    
    return answer