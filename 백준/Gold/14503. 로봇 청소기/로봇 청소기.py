import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
r, c, d = map(int, sys.stdin.readline().split())

graph = [list(map(int, sys.stdin.readline().split())) for i in range(n)]

def dfs(x, y, d) :
    
    stack = deque()
    
    stack.append((x, y, d))
    count = 0
    
    row = [0, -1, 0, 1]
    col = [-1, 0, 1, 0]
    
    b_row = [1, 0, -1, 0]
    b_col = [0, -1, 0, 1]
    
    while stack :
        a, b, c = stack.pop()
        
        if graph[a][b] == 0 :
            graph[a][b] = -1
            count += 1
                      
        b_x = a + b_row[c]
        b_y = b + b_col[c]
        
        flag = 0
        k = c
        
        for i in range(4) :         
            if graph[a + row[k]][b + col[k]] == 0 :
                flag = 1
                break 
                
            k = (k - 1) % 4 
            
        newx = a + row[k]
        newy = b + col[k]
        
        if 0 <= newx < n and 0 <= newy < m :
            if graph[newx][newy] == 0 :
                new_d = (k - 1) % 4
                stack.append((newx, newy, new_d))
                
            elif flag == 0 :
                if graph[b_x][b_y] == 1 :
                    break
                    
                else :
                    stack.append((b_x, b_y, c))
        
    return count


result = dfs(r, c, d)   

print(result)