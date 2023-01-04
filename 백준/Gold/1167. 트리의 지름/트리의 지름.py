import sys
from collections import deque

n = int(sys.stdin.readline())

matrix = [[] * (n + 1) for i in range(n + 1)]

for i in range(n) :
    
    inform = list(map(int, sys.stdin.readline().split())) 
    i = 1
    
    while i < len(inform) - 1 :
        matrix[inform[0]].append((inform[i], inform[i+1]))
        i += 2
        
def dfs(x, matrix) :
    
    stack = deque()
    visited = [-1] * (n + 1) 
    
    stack.append(x)
    visited[x] = 0 
    
    max_val, idx = 0, 0
    
    while stack :
        a = stack.pop()
        for p, w in matrix[a] :
            if visited[p] == -1 :
                visited[p] = visited[a] + w
                stack.append(p)
                if max_val < visited[p] :
                    max_val = visited[p]
                    idx = p
            
    return max_val, idx
       
a, b = dfs(1, matrix)
c, d = dfs(b, matrix)

print(c)
                