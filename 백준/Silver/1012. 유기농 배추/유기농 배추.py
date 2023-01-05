import sys

num = int(sys.stdin.readline())

row = [-1, 1, 0, 0]
col = [0, 0, 1, -1]

def bfs(x, y) :
    
    queue = [(x, y)]
    matrix[x][y] = 0 
    
    while queue :
        x, y = queue.pop(0)
        
        for i in range(4) :
            nx = x + row[i]
            ny = y + col[i]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= m :
                continue
                
            if matrix[nx][ny] == 1 :
                queue.append((nx,ny))
                matrix[nx][ny] = 0

for i in range(num) :
    
    n, m, k = map(int, sys.stdin.readline().split())
    
    matrix = [[0] * m for i in range(n)]
    count = 0
    
    for i in range(k) :
        
        x, y = map(int, sys.stdin.readline().split())
        matrix[x][y] = 1
        
        
    for j in range(n) :
        for k in range(m) :
            if matrix[j][k] == 1:
                bfs(j, k)
                count += 1
    
    print(count)
