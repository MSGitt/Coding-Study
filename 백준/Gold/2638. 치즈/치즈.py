import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
matrix = [list(map(int, sys.stdin.readline().split())) for i in range(n)]

def bfs(x, y) :
    
    visited = [[0] * (m) for i in range(n)]   
    queue = deque()
    row = [1, -1, 0, 0]
    col = [0, 0, 1, -1]
    
    visited[x][y] = 1
    queue.append((x, y))
    
    
    while queue :
        a, b = queue.popleft()
        for i in range(4) :
            newx = a + row[i]
            newy = b + col[i]
            if 0 <= newx < n and 0 <= newy < m and visited[newx][newy] == 0:
                if matrix[newx][newy] >= 1:
                    matrix[newx][newy] += 1
                    
                else:
                    visited[newx][newy] = 1
                    queue.append((newx, newy))
                    
result = 0

while True :
       
    bfs(0, 0)
    flag = 0
    
    for i in range(n):
        for j in range(m):
            if matrix[i][j] >= 3 :
                matrix[i][j] = 0
                flag = 1
            elif matrix[i][j] == 2 :
                matrix[i][j] = 1
                
    if flag == 1 :
        result += 1
        
    else : 
        break
        
print(result)