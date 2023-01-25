from collections import defaultdict

def solution(gems):
    answer = []
    
    n = len(set(gems))
    
    count = defaultdict(int)
    
    before, end = 0, 0
    result = len(gems) + 1
    
    for i in range(len(gems)) :   
        
        while len(count) < n and end < len(gems) :
            count[gems[end]] += 1
            end += 1
            
        if len(count) == n :
            if result > end - i :
                result = end - i
                answer = [i + 1, end]
                
        count[gems[i]] -= 1
        
        if count[gems[i]] == 0 :
            del count[gems[i]]
    
    return answer