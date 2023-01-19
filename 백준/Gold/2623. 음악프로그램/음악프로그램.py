import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

indegree = [0] * (n + 1)
graph = [[] for i in range(n + 1)]

for i in range(m) :
    
    a = list(map(int, sys.stdin.readline().split()))
    for i in range(1, a[0]) :
        graph[a[i]].append(a[i+1])
        indegree[a[i+1]] += 1
    
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

if len(visited) != n :
    print(0)

else :
    for i in visited :
        print(i)