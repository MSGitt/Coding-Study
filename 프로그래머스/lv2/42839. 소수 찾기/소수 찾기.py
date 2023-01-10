import math
from itertools import permutations

def solution(numbers):
    
    number = list(numbers)
    
    num = []
    
    
    for i in range(1, len(numbers) + 1) :
        num += list(permutations(number, i))
        
    num = [int(''.join(i)) for i in num]
    
    result = []
    
    for i in num :
        flag = 0
        
        if i < 2 :
            continue 
            
        for j in range(2, int(math.sqrt(i)) + 1) :
            if i % j == 0 :
                flag = 1
                break
                
        if flag == 0 :
            result.append(i)
            
        
    return len(set(result))              