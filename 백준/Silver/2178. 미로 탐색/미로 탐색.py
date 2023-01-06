import sys
from collections import deque


n, m = map(int, sys.stdin.readline().split())

matrix = [list(map(int, sys.stdin.readline().rstrip())) for i in range(n)]
visited = [[0] * m for i in range(n) ]

def bfs(x, y, matrix, visited, n, m) :
    
    row = [1, -1, 0, 0]
    col = [0, 0, 1, -1]
    
    queue = deque()
    
    queue.append((x, y))
    visited[x][y] = 1
    
    while queue :
        a, b = queue.popleft()
        for i in range(4) :
            newx = a + row[i]
            newy = b + col[i]
            if 0 <= newx < n and 0 <= newy < m and matrix[newx][newy] == 1 and visited[newx][newy] == 0:
                queue.append((newx, newy))
                visited[newx][newy] = 1
                matrix[newx][newy] = matrix[a][b] + 1 
                
bfs(0, 0, matrix, visited, n, m)

print(matrix[n-1][m-1])


            
        