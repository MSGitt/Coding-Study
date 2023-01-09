def solution(strings, n):
    
    answer = []
    
    for i in strings :
        answer.append(i)
        
    k = sorted(answer)
    
    
    return sorted(k, key = lambda x : x[n])