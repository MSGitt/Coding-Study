import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

matrix = [list(map(int, input())) for i in range(n)]
visited = [[[0] * 2 for i in range(m)] for i in range(n)]

def bfs(x, y, z, matrix, visited, n, m) :
    
    queue = deque()
    row = [1, -1, 0, 0]
    col = [0, 0, 1, -1]
    
    queue.append((x, y, z))
    visited[0][0][0] = 1
    
    while queue : 
        a, b, c = queue.popleft()
        if a == n - 1 and b == m - 1 :
            return visited[a][b][c]
        
        for i in range(4) :
            newx = a + row[i]
            newy = b + col[i]
            if 0 <= newx < n and 0 <= newy < m :
                if c == 0 and matrix[newx][newy] == 1 :
                    visited[newx][newy][1] = visited[a][b][c] + 1
                    queue.append((newx, newy, 1))
                    
                elif visited[newx][newy][c] == 0 and matrix[newx][newy] == 0 :
                    visited[newx][newy][c] = visited[a][b][c] + 1
                    queue.append((newx, newy, c))
                    
                else :
                    continue
                                        
    return -1 

print(bfs(0, 0, 0, matrix, visited, n, m))
        