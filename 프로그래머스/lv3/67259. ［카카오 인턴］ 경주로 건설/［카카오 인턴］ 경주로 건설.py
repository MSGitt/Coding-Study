from collections import deque 

def bfs(x, y, board, n) :
    
    queue = deque()
    cost = [[[float('inf')] * n for i in range(n)] for j in range(4)]
    row = [0, 0, 1, -1]
    col = [1, -1, 0, 0]
    
    queue.append((x, y, 0, -1))
    
    for i in range(4) :
        cost[i][0][0] = 0
    
    while queue :
        a, b, k, c = queue.popleft()  
        
        if a == n - 1 and b == n - 1:
            continue
        
        for i in range(4) :
            newx = a + row[i]
            newy = b + col[i]
            newc = i
            
            if newx < 0 or newx >= n or newy < 0 or newy >= n :
                continue
                
            if board[newx][newy] == 1 :
                continue
            
            if newc == c or c == -1 :
                ncost = k + 100
                
            else : 
                ncost = k + 600
                
            if ncost < cost[newc][newx][newy] :               
                cost[newc][newx][newy] = ncost
                queue.append((newx, newy, ncost, newc))
    
    answer = float('inf')
    
    for z in range(4) :
        if answer > cost[z][n-1][n-1]:
            answer = cost[z][n-1][n-1] 
            
    return answer

def solution(board):
    
    n = len(board)
    
    result = bfs(0, 0, board, n)
    
    return result