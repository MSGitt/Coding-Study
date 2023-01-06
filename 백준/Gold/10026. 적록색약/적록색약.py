import sys
from collections import deque
import copy

n = int(sys.stdin.readline())

matrix1 = [list(sys.stdin.readline().rstrip()) for i in range(n)] 
matrix2 = copy.deepcopy(matrix1)

for i in range(n) :
    for j in range(n) :
        if matrix1[i][j] == 'G' :
            matrix2[i][j] = 'R'

visited1 = [[0]*n for i in range(n)]
visited2 = [[0]*n for i in range(n)]

def bfs(x, y, matrix, visited) :
    
    queue = deque()
    row = [1, -1, 0, 0]
    col = [0, 0, 1, -1]
    
    queue.append((x, y))
    visited[x][y] = 1 
    
    while queue :
        a, b = queue.popleft()
        color = matrix[a][b]
        for i in range(4) :
            newx = a + row[i]
            newy = b + col[i]
            if 0 <= newx < n and 0 <= newy < n and visited[newx][newy] == 0 and color == matrix[newx][newy] :
                queue.append((newx, newy))
                visited[newx][newy] = 1
                
                
    return 
                              
count1 = 0 
count2 = 0
                
for i in range(n) :
    for j in range(n) :
        if visited1[i][j] == 0 :
            bfs(i, j, matrix1, visited1)
            count1 += 1
            
        if visited2[i][j] == 0 :
            bfs(i, j, matrix2, visited2)
            count2 += 1
            
print(count1, count2)

                
    