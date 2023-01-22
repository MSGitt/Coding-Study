import sys

n, m, r = map(int, sys.stdin.readline().split())

matrix = [list(map(int, sys.stdin.readline().split())) for i in range(n)]

rotate = 0

row = [1, 0, -1, 0]
col = [0, 1, 0, -1]

while rotate < r :
    
    visited = [[0] * m for i in range(n)]
    start_x, start_y = 0, 0 
    
    direction = 0
    x, y = 0, 0
    temp = matrix[x][y]
    
    count = 0
    
    while count < n * m :
     
        while True :
            newx = x + row[direction]
            newy = y + col[direction]       
            if 0 <= newx < n and 0 <= newy < m and visited[newx][newy] == 0 :
                visited[newx][newy] = 1
                
                new_temp = matrix[newx][newy]
                matrix[newx][newy] = temp
                temp = new_temp
            
                x, y = newx, newy
                count += 1              
            
            else :
                direction = (direction + 1) % 4
            
            if newx == start_x and newy == start_y :
                x, y = newx + 1, newy + 1
                start_x, start_y = x, y 
                temp = matrix[x][y]                             
                break    
                
    rotate += 1

for i in matrix :
    print(*i)   