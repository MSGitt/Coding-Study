def solution(n, s):
    answer = []
    
    for i in range(n) :   
        temp = s // n
        
        if temp == 0 :
            return [-1] 
        
        answer.append(temp)
        
        n -= 1
        s -= temp 
         
    return answer