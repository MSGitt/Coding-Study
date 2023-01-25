import heapq
from collections import defaultdict

def dijkstra(x, matrix, n) :
    
    visited = [float('inf')] * (n + 1)
    queue = []
    
    heapq.heappush(queue, (0, x))
    visited[x] = 0
    
    while queue :
        dist, node = heapq.heappop(queue) 
        
        if visited[node] < dist :
            continue 
            
        for i, j in matrix[node] :
            cost = visited[node] + j
            if visited[i] > cost :
                visited[i] = cost
                heapq.heappush(queue, (cost, i))
    
    return visited

def solution(n, s, a, b, fares):
    
    matrix = defaultdict(list)
    
    for i in fares :
        
        matrix[i[0]].append((i[1], i[2]))
        matrix[i[1]].append((i[0], i[2]))
    
    distance = []
    
    for i in range(1, n + 1) :
        distance.append(dijkstra(i, matrix, n))
       
    result = float('inf')
    
    for i in range(1, n + 1) :
        result = min(result, distance[s-1][i] + distance[i-1][a] + distance[i-1][b])
    
    return result   