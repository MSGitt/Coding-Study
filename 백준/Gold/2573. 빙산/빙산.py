import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for i in range(n)]

def bfs(x, y, visited) :
    
    queue = deque()   
    count = []
    row = [1, -1, 0, 0]
    col = [0, 0, 1, -1]
    
    queue.append((x, y))
    visited[x][y] = 1
    
    while queue :
        a, b = queue.popleft()
        cnt = 0
        for i in range(4) :
            newx = a + row[i]
            newy = b + col[i]
            if 0 <= newx < n and 0 <= newy < m :
                if not graph[newx][newy] :
                    cnt += 1
                    
                elif graph[newx][newy] and not visited[newx][newy] :
                    queue.append((newx, newy))
                    visited[newx][newy] = 1
                    
        if cnt != 0 :
            count.append((a, b, cnt))
            
    for x, y, cnt in count :
        graph[x][y] = max(0, graph[x][y] - cnt)
        
ice = []

for i in range(n) :
    for j in range(m) :
        if graph[i][j] != 0 :
            ice.append((i, j))
            
year = 0

while ice :
    
    visited = [[0] * m for i in range(n)]
    count = 0
    del_count = []
    
    for i, j in ice :
        if graph[i][j] and visited[i][j] == 0 :
            bfs(i, j, visited)
            count += 1
            
        if graph[i][j] == 0 :
            del_count.append((i, j))
            
    if count >= 2 :           
        print(year)
        break
        
    ice = sorted(list(set(ice) - set(del_count)))
    
    year += 1
    
if count < 2 :
    print(0)                