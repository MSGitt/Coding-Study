import sys
import heapq

n, m = map(int, sys.stdin.readline().split())

graph = [[] for i in range(n + 1)]
indegree = [0] * (n + 1)

for i in range(m) :
    a, b = map(int, sys.stdin.readline().split())
    
    graph[a].append(b)
    indegree[b] += 1
      
def sort() :
    
    queue = []
    result = []
    
    for i in range(1, n + 1) :
        if indegree[i] == 0 :
            heapq.heappush(queue, i)         
    while queue :
        a = heapq.heappop(queue)
        result.append(a)
        for i in graph[a] :
            indegree[i] -= 1          
            if indegree[i] == 0 :
                heapq.heappush(queue, i)
                
    return result
      
result = sort()
print(*result)