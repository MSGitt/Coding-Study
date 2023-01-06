import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
visited = [0] * 1000001

def bfs(x, k) :
    
    queue = deque()
    queue.append(x)
 
    
    while queue :
        c = queue.popleft()
            
        if c == k :
            return visited[c]
            
        else :
            for i in (c-1, c + 1, c * 2) :
                if 0 <= i <= 100000 and visited[i] == 0 :
                    queue.append(i)
                    visited[i] = visited[c] + 1
                                   
print(bfs(n, k))           
    