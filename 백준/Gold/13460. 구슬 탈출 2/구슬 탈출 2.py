import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
graph = [list(sys.stdin.readline().rstrip()) for i in range(n)]

xr, yr, xb, yb = 0, 0, 0, 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 'R' :
            xr, yr = i, j
        elif graph[i][j] == 'B' :
            xb, yb = i, j
         
    
def bfs(xr, yr, xb, yb) :
    
    row = [1, -1, 0, 0]
    col = [0, 0, 1, -1]
    
    queue = deque()
    visited = []
    
    count = 0
    
    queue.append((xr, yr, xb, yb))
    visited.append((xr, yr, xb, yb))
    
    while queue :
        for k in range(len(queue)) :
            xr, yr, xb, yb = queue.popleft()
            if count > 10 :
                print(-1)
                return
            
            if graph[xr][yr] == 'O' :
                print(count)
                return
            
            for i in range(4) : 
                nxr, nyr = xr, yr
                while True :
                    nxr += row[i]
                    nyr += col[i]
                    if graph[nxr][nyr] == '#' : 
                        nxr -= row[i]
                        nyr -= col[i]
                        break
                    if graph[nxr][nyr] == 'O' :
                        break
                nxb, nyb = xb, yb
                while True :
                    nxb += row[i]
                    nyb += col[i]
                    if graph[nxb][nyb] == '#' : 
                        nxb -= row[i]
                        nyb -= col[i]
                        break
                    if graph[nxb][nyb] == 'O' :
                        break
                        
                if graph[nxb][nyb] == 'O' :
                    continue
                    
                if nxr == nxb and nyr == nyb :
                    if abs(nxr - xr) + abs(nyr - yr) > abs(nxb - xb) + abs(nyb - yb) :
                        nxr -= row[i]
                        nyr -= col[i]
                        
                    else :
                        nxb -= row[i]
                        nyb -= col[i]
                        
                if (nxr, nyr, nxb, nyb) not in visited :
                    queue.append((nxr, nyr, nxb, nyb))
                    visited.append((nxr, nyr, nxb, nyb))
                    
        count += 1  
                    
    print(-1)  
    
bfs(xr, yr, xb, yb)   