from collections import deque

def dfs(x, visited, computers) :
    
    stack = deque()
    stack.append(x)
    
    while stack :
        a = stack.pop()
        if visited[a] == 0 :
            visited[a] = 1
            for i in range(len(computers[a])) :
                if a != i and computers[a][i] == 1 and visited[i] == 0 :
                    stack.append(i)  
                                                                 
def solution(n, computers):
                       
    visited = [0] * n
    count = 0
                       
    for i in range(n) :    
        if not visited[i] :
            dfs(i, visited, computers)
            count += 1
    
    return count
