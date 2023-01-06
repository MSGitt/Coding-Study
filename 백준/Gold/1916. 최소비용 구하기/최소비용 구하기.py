import sys
import heapq

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

matrix = [[] for i in range(n + 1)]

for i in range(m) :
    
    a, b, c = map(int, sys.stdin.readline().split())
    matrix[a].append((b, c))
    
start, end = map(int, sys.stdin.readline().split())

def dijkstra(x, matrix) : 
    
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

result = dijkstra(start, matrix)

print(result[end])               