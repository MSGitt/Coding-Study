from collections import defaultdict

def solution(n, results):
    
    win = defaultdict(set)
    lose = defaultdict(set)
    
    answer = 0
    
    for i, j in results :
        win[i].add(j)
        lose[j].add(i)
    
    for i in range(1, n + 1) :
        for j in win[i] :
            lose[j].update(lose[i])
        
        for k in lose[i] :
            win[k].update(win[i])
    
    for i in range(1, n + 1) :
        if len(win[i]) + len(lose[i]) == n - 1 :
            answer += 1
            
    return answer
    