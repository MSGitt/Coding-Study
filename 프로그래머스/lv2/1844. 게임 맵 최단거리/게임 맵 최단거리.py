from collections import deque

def bfs(x, y, maps, m, n) :
    
    queue = deque()
    row = [1, -1, 0, 0]
    col = [0, 0, 1, -1]
    
    queue.append((x, y))
    
    while queue :
        a, b = queue.popleft()
        for i in range(4) :
            newx = a + row[i]
            newy = b + col[i]
            if 0 <= newx < m and 0 <= newy < n and maps[newx][newy] == 1 :
                maps[newx][newy] += maps[a][b]
                queue.append((newx, newy))
        
    return maps[-1][-1]


def solution(maps):
    
    m = len(maps)
    n = len(maps[0])
    
    result = bfs(0, 0, maps, m, n) 
    
    if result == 1 :
        return -1 
    
    return result