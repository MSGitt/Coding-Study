import sys
import copy
from collections import deque
from itertools import combinations

n, m = map(int, sys.stdin.readline().split())

matrix = [list(map(int, sys.stdin.readline().split())) for i in range(n)]

virus = deque()
wall = deque()

for i in range(n) : 
    for j in range(m) : 
        if matrix[i][j] == 2 :
            virus.append((i, j))
            
        elif matrix[i][j] == 0 :
            wall.append((i, j))
            
def bfs(queue, matrix) :
    
    row = [1, -1, 0, 0]
    col = [0, 0, 1, -1]
       
    while queue :
        a, b = queue.popleft()
        for i in range(4) :
            newx = a + row[i]
            newy = b + col[i]
            if 0 <= newx < n and 0 <= newy < m and matrix[newx][newy] == 0 :
                matrix[newx][newy] = 2
                queue.append((newx, newy))
    
    count = 0
    for i in range(n) :
        for j in range(m) :
            if matrix[i][j] == 0 :
                count += 1
                
    return count

result = 0

for i in list(combinations(wall, 3)) :   
    m1 = copy.deepcopy(matrix)
    q1 = copy.deepcopy(virus)
    
    for j in range(3) :
        x, y = i[j][0], i[j][1]
        m1[x][y] = 1
        
    result = max(result, bfs(q1, m1))
    
print(result)