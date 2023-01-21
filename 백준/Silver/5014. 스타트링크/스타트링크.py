import sys
from collections import deque

f, s, g, u, d = map(int, sys.stdin.readline().split())

def bfs(s, g, u, d) :
    
    queue = deque()
    visited = [0] * (f + 1)
    visited[0] = 1
    
    queue.append(s)
    visited[s] = 1
    
    while queue :
        a = queue.popleft()
        
        for i in (u, -d) :
            new = a + i
            if 0 <= new <= f and visited[new] == 0 :
                visited[new] = visited[a] + 1
                queue.append(new)
                
    return visited[g]

result = bfs(s, g, u, d)

if result == 0 :
    print('use the stairs')

else :
    print(result - 1)           