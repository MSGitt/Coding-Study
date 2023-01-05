import sys
from collections import deque

n = int(sys.stdin.readline())
matrix = [[] for i in range(n+1)]

for i in range(n - 1) : 
    
    a, b, c = map(int, sys.stdin.readline().split())
    matrix[a].append((b, c))
    matrix[b].append((a, c))
    
def dfs(x, matrix) :
    
    visited = [-1] * (n + 1)
    stack = deque()
    
    max_val, idx = 0, 0
    
    stack.append(x) 
    visited[x] = 0
    
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
    