import sys
import heapq

n, e = map(int, sys.stdin.readline().split())
matrix = [[] for i in range(n + 1)]

for i in range(e) :
    
    x, y, cost = map(int, sys.stdin.readline().split())
    matrix[x].append((y, cost))
    matrix[y].append((x, cost))
    
def dijkstra(x) :
    
    visited = [float('inf')] * (n + 1)
    queue = []
    
    visited[x] = 0
    heapq.heappush(queue, (0, x))
    
    while queue :
        w, p = heapq.heappop(queue)
        
        if visited[p] < w :
            continue 
            
        for new_p, new_w in matrix[p] :
            if visited[new_p] > visited[p] + new_w :
                visited[new_p] = visited[p] + new_w 
                heapq.heappush(queue, (visited[p] + new_w, new_p))
                
    return visited

k1, k2 = map(int, sys.stdin.readline().split())

v = dijkstra(1)
v1 = dijkstra(k1)
v2 = dijkstra(k2)

r1 = v[k1] + v1[k2] + v2[n]
r2 = v[k2] + v2[k1] + v1[n]

result = (min(r1, r2))

if result < float('inf') :
    print(result)
    
else: 
    print(-1)