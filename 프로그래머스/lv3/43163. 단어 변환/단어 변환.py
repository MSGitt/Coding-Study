from collections import deque 

def bfs(x, target, words) : 
    
    queue = deque()
    visited = [0] * len(words)
    
    queue.append((x, 0))
    
    while queue : 
        w, d = queue.popleft()
        if w == target : 
            return d 
        
        for i in range(len(words)) :
            temp = 0
            
            if not visited[i] : 
                for j in range(len(w)) :
                    if w[j] != words[i][j] :
                        temp += 1
                        
                if temp == 1 :
                    queue.append((words[i], d + 1))
                    visited[i] = 1


def solution(begin, target, words):
    
    result = bfs(begin, target, words)
    
    if not result :
        return 0
    
    return result
    