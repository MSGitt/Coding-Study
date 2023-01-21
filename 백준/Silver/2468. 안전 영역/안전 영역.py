import sys
from collections import deque

n = int(sys.stdin.readline())

graph = [list(map(int, sys.stdin.readline().split())) for i in range(n)]

def bfs(x, y, visited, k) :
            
    queue = deque()
    row = [1, -1, 0, 0]
    col = [0, 0, 1, -1]
                        
    queue.append((x, y))
    visited[x][y] = 1
    
    while queue :
        a, b = queue.popleft()
        for i in range(4) :
            newx = a + row[i]
            newy = b + col[i]
            if 0 <= newx < n and 0 <= newy < n and visited[newx][newy] == 0 :
                visited[newx][newy] = 1
                queue.append((newx, newy))

result = 0
                
for i in range(101) :
    visited = [[0] * n for i in range(n)]
    count = 0
    
    for j in range(n) :
        for k in range(n) :
            if graph[j][k] <= i :
                visited[j][k] = 1
                
    for j in range(n) :
        for k in range(n) :
            if visited[j][k] == 0 :
                bfs(j, k, visited, i)
                count += 1
                
    result = max(result, count)
    
print(result)