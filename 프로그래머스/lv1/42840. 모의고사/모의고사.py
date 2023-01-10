def solution(answers):
    answer = []
    
    n1 = [1, 2, 3, 4, 5]
    n2 = [2, 1, 2, 3, 2, 4, 2, 5]
    n3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    c1, c2, c3 = 0, 0, 0
    
    for i in range(len(answers)) :
        if answers[i] == n1[i % 5] :
            c1 += 1
            
        if answers[i] == n2[i % 8] :
            c2 += 1
            
        if answers[i] == n3[i % 10] :
            c3 += 1
            
    k = max(c1, c2, c3)
    
    if c1 == k :
        answer.append(1)
    
    if c2 == k :
        answer.append(2)
        
    if c3 == k :
        answer.append(3)
    
    return answer