import heapq
from collections import Counter

def dijkstra(x, vertex, visited) :
    
    queue = []
    
    heapq.heappush(queue, (0, x))
    visited[x] = 0
    
    while queue :
        dist, node = heapq.heappop(queue)
        
        if visited[node] < dist :
            continue
            
        for i, j in vertex[node] :
            cost = visited[node] + j
            if cost < visited[i] :
                visited[i] = cost
                heapq.heappush(queue, (cost, i))


def solution(n, edge):
    
    visited = [float('inf')] * (n + 1)
    matrix = [[] * (n + 1) for i in range(n + 1)]
    
    for i in edge :
        
        matrix[i[0]].append((i[1], 1))
        matrix[i[1]].append((i[0], 1))
        
    dijkstra(1, matrix, visited)
    
    answer = 0
    
    a = Counter(visited) 
    del a[float('inf')]

    temp = max(a.keys())
       
    return a[temp]