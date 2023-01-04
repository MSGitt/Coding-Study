import sys
import heapq

v, e = map(int, sys.stdin.readline().split())
k = int(sys.stdin.readline())

matrix = [[] * (v + 1) for i in range(v + 1)]
visited = [float('inf')] * (v + 1)

for i in range(e) :
    
    a, b, c = map(int, sys.stdin.readline().split())
    matrix[a].append((b, c))
    
def find(x, matrix, visited) :
    
    queue = []
    
    visited[x] = 0
    heapq.heappush(queue, (0, x))
    
    while queue :
        w, p = heapq.heappop(queue)
            
        for new_p, new_w in matrix[p] : 
            weight = w + new_w
            if weight < visited[new_p] :
                visited[new_p] = weight
                heapq.heappush(queue, (weight, new_p))
                                                   
    return visited 

result = find(k, matrix, visited) 

for i in range(1, len(result)) :
    if result[i] == float('inf') :
        print('INF')

    else :
        print(result[i])
                                   
