import sys
from collections import deque


n, m = map(int, sys.stdin.readline().split())
visited = [0] * 100001

def bfs(n, visited, m) :
    
    queue = deque()
    
    queue.append(n)
    visited[n] = 1
    
    while queue :
        a = queue.popleft()
        
        if a == m :
            return visited[a]
        
        for i in (a + 1, a - 1, 2*a) :
            
            if 0 <= i <= 100000 and visited[i] == 0 :
                
                if i == 2 * a :
                    visited[i] = visited[a]
                    queue.appendleft(i)
                    
                else : 
                    visited[i] = visited[a] + 1
                    queue.append(i)

print(bfs(n, visited, m) - 1)