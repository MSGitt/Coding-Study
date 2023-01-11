from collections import deque

def dfs(x, visited, computers) :
    
    stack = deque()
    
    visited[x] = 1
    stack.append(x)
    
    while stack :
        a = stack.pop()
        for i in range(len(computers[a])) :
            if a != i and computers[a][i] == 1 and visited[i] == 0 :
                visited[i] = 1
                stack.append(i)  
                                                                 
def solution(n, computers):
                       
    visited = [0] * n
    count = 0
                       
    for i in range(n) :    
        if not visited[i] :
            dfs(i, visited, computers)
            count += 1
    
    return count
