import sys
from collections import deque

m, n = map(int, sys.stdin.readline().split())

graph = [list(map(int, sys.stdin.readline().rstrip())) for i in range(m)]

def bfs(x, y) :
    
    queue = deque()
    row = [1, -1, 0, 0]
    col = [0, 0, 1, -1]
        
    queue.append((x, y))
    graph[x][y] = 2
    
    while queue :
        a, b = queue.popleft()
        for i in range(4) :
            newx = a + row[i]
            newy = b + col[i]
            if 0 <= newx < m and 0 <= newy < n and graph[newx][newy] == 1 :
                graph[newx][newy] = graph[a][b] + 1
                queue.append((newx, newy))
                
    return graph[-1][-1] - 1

result = bfs(0, 0)

print(result)