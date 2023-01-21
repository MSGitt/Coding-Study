import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())

def bfs(x, k) :
    
    queue = deque()
    visited = [0] * 100001
    
    queue.append(x)
    count = 0
    
    while queue :
        a = queue.popleft()
        
        if a == k :
            return visited[k]
        
        for i in (a-1, a+1, 2*a) :
            if 0 <= i < 100001 and visited[i] == 0 :
                queue.append(i)
                visited[i] = visited[a] + 1
                
result = bfs(n, k)   

print(result)