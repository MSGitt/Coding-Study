import sys
from collections import deque, defaultdict

n, m = map(int, sys.stdin.readline().split())
graph = defaultdict(list)
indegree = [0] * (n + 1)

result = [0] * (n + 1)

for i in range(m) :
    
    a, b = map(int, sys.stdin.readline().split())
    
    graph[a].append(b) 
    indegree[b] += 1
       
def sort() :
    
    queue = deque()
    
    for i in range(1, n + 1) :
        if indegree[i] == 0 :
            queue.append((i, 1))
                     
    while queue :
        a, b = queue.popleft()
        result[a] = b
        
        for i in graph[a] :
            indegree[i] -= 1
            if indegree[i] == 0 :
                queue.append((i, b + 1))
                
sort()

print(*result[1:])  