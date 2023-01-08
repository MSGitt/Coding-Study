import sys

r, c, t = map(int, sys.stdin.readline().split())

matrix = [list(map(int, sys.stdin.readline().split())) for i in range(r)]

k1, k2 = 0, 0

for i in range(r) : 
    if matrix[i][0] == -1 :
        k1 = i
        k2 = i + 1
        break
                               
def dust_move() :
    
    row = [1, -1, 0, 0]
    col = [0, 0, 1, -1]
    
    temp = [[0] * c for i in range(r)]
    
    for i in range(r) :
        for j in range(c) :
            if matrix[i][j] >= 5 :
                number = matrix[i][j] // 5
                for k in range(4) :
                    newx = i + row[k]
                    newy = j + col[k]                    
                    if 0 <= newx < r and 0 <= newy < c and matrix[newx][newy] != -1 :
                        temp[newx][newy] += number
                        matrix[i][j] -= number
                
    for i in range(r):
        for j in range(c):
            matrix[i][j] += temp[i][j]
        
def air_moveup() :    
    
    row = [0, -1, 0, 1]
    col = [1, 0, -1, 0]
    
    direction = 0
    temp = 0
    
    x, y = k1, 1
        
    while True :
        newx = x + row[direction]
        newy = y + col[direction]
        
        if x == k1 and y == 0 :
            break
            
        if newx < 0 or newx >= r or newy < 0 or newy >= c:
            direction += 1
            continue
            
        matrix[x][y], temp = temp, matrix[x][y]
        x = newx  
        y = newy
    
def air_movedown() :    
    
    row = [0, 1, 0, -1]
    col = [1, 0, -1, 0]
    
    direction = 0
    temp = 0
    
    x, y = k2, 1
        
    while True :
        newx = x + row[direction]
        newy = y + col[direction]
        
        if x == k2 and y == 0 :
            break
            
        if newx < 0 or newx >= r or newy < 0 or newy >= c:
            direction += 1
            continue
            
        matrix[x][y], temp = temp, matrix[x][y]
        x = newx  
        y = newy
        
for i in range(t) :
    
    dust_move()
    air_moveup()
    air_movedown()
    
matrix[k1][0] = matrix[k2][0] = 0

print(sum(map(sum, matrix)))   