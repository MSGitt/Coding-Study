from itertools import permutations

def check(i, word) :
    
    for j in range(len(i)) :
        if len(i[j]) != len(word[j]) :
            return False
        
        for k in range(len(i[j])) : 
            if word[j][k] != '*' and i[j][k] != word[j][k] :
                return False
        
    return True
    
    
def solution(user_id, banned_id):
    
    answer = []
    
    for i in permutations(user_id, len(banned_id)) :
        if check(i, banned_id) :
            if set(i) not in answer :
                answer.append(set(i))
         
    return len(answer)