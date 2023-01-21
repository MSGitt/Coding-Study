import sys
from collections import deque, defaultdict

n = int(sys.stdin.readline())

x, y = map(int, sys.stdin.readline().split())

m = int(sys.stdin.readline())
graph = defaultdict(list)

for i in range(m) :
    a, b = map(int, sys.stdin.readline().split())
    
    graph[a].append(b)
    graph[b].append(a)
    
def bfs(x) :
    
    visited = [0] * (n + 1) 
    queue = deque()
    
    visited[x] = 1
    queue.append(x)
    
    while queue :
        a = queue.popleft()
        for i in graph[a] :
            if visited[i] == 0 :
                visited[i] = visited[a] + 1
                queue.append(i)
                
    return visited

result = bfs(x)

if result[y] == 0 :
    print(-1)

else :
    print(result[y] - 1)