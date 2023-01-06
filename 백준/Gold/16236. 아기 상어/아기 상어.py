import sys
from collections import deque

n = int(sys.stdin.readline())

matrix = [list(map(int, sys.stdin.readline().split())) for i in range(n)]
visited = [[0] * n for i in range(n)]
distance = [[0] * n for i in range(n)]

x, y = 0, 0

for i in range(n) :
    for j in range(n) :
        if matrix[i][j] == 9 :
            x = i
            y = j
            
def bfs(x, y, matrix, n, size) :
    
    queue = deque()
    
    row = [1, -1, 0, 0]
    col = [0, 0, 1, -1]

    result = []
    visited = [[0] * n for i in range(n)]
    distance =  [[0] * n for i in range(n)]

    
    queue.append((x, y))
    visited[x][y] = 1
    matrix[x][y] = 0
        
    while queue :
        a, b = queue.popleft()
        for i in range(4):
            newx = a + row[i]
            newy = b + col[i]
            if 0 <= newx < n and 0 <= newy < n and visited[newx][newy] == 0 :
                if matrix[newx][newy] <= size :
                    visited[newx][newy] = 1
                    queue.append((newx, newy))
                    distance[newx][newy] = distance[a][b] + 1
                    if matrix[newx][newy] < size and matrix[newx][newy] != 0 :
                        result.append((newx, newy, distance[newx][newy]))
                        
                        
    result.sort(key = lambda x : (-x[2], -x[0], -x[1]))                 
    
     
    return result


count = 0
result = 0
size = 2

while True :
    
    distances = bfs(x, y, matrix, n, size)
    
    if len(distances) == 0 :
        break
        
    newx, newy, dist = distances.pop()
 
    result += dist 
    
    
    x, y = newx, newy
    count += 1
    
    if count == size :
        size += 1
        count = 0

print(result)
    
                     
    
    