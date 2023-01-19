import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

indegree = [0] * (n + 1)
graph = [[] for i in range(n + 1)]

for i in range(m) :
    
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    
    indegree[b] += 1
    
def sort() :
    
    queue = deque()
    visited = []
    
    for i in range(1, n + 1) :
        if indegree[i] == 0 :
            queue.append(i)
            
    while queue :
        a = queue.popleft()
        visited.append(a)
        
        for i in graph[a] :
            indegree[i] -= 1
            if indegree[i] == 0 :
                queue.append(i)
                
    return visited

visited = sort()

print(*visited)