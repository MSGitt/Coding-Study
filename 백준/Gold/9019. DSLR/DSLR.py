import sys
from collections import deque

n = int(sys.stdin.readline())

def bfs(x, y) :
    
    queue = deque()
    
    queue.append((x, ''))
    visited = [0] * 10000
    
    while queue :
        a, b = queue.popleft()
        visited[a] = 1
        
        if a == y :
            print(b)
            break
            
        c = (2*a) % 10000
        if visited[c] == 0 :
            queue.append((c, b + 'D'))
            visited[c] = 1
            
        c = (a-1) % 10000
        if visited[c] == 0 :
            queue.append((c, b + 'S'))
            visited[c] = 1
            
        c = (10*a+(a//1000))%10000
        if visited[c] == 0 :
            queue.append((c, b + 'L'))
            visited[c] = 1
            
        c = (a//10+(a%10)*1000)%10000
        if visited[c] == 0 :
            queue.append((c, b + 'R'))
            visited[c] = 1
            
for i in range(n) :
    
    a, b = map(int, sys.stdin.readline().split())
    bfs(a, b)
    
    