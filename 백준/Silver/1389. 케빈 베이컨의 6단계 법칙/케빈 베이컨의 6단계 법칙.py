import sys
from collections import deque


m, n = map(int, sys.stdin.readline().split())

matrix = [[] for i in range(m+1)]

for i in range(n) :
    
    a, b = map(int, sys.stdin.readline().split())
    matrix[a].append(b)
    matrix[b].append(a)
    
def bfs(matrix, num) :
    
    number = [0] * (m+1)
    queue = deque()
    visited = []
    
    queue.append(num) 
    visited.append(num)
    
    while queue :
        a = queue.popleft()
        for v in matrix[a] :
            if v not in visited :
                visited.append(v)
                queue.append(v)
                number[v] = number[a] + 1
                
    return sum(number)

result = []
for i in range(1, m + 1) :
    result.append((i, bfs(matrix, i)))
    
result.sort(key = lambda x : (x[1], x[0]))

print(result[0][0])
            
        
            