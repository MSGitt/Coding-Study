import sys
from collections import deque

t = int(sys.stdin.readline())

def bfs(x, y, x2, y2) :
    
    queue = deque()
    queue.append((x, y))
    
    while queue :
        a, b = queue.popleft()
        if abs(x2 - a) + abs(y2 - b) <= 1000 :
            print('happy')
            return 
        
        for i in range(n) :
            if visited[i] == 0 :
                x1, y1 = graph[i]
                if abs(x1 - a) + abs(y1 - b) <= 1000 :
                    visited[i] = 1
                    queue.append((x1, y1))
                    
    print('sad')
    return
        

for i in range(t) :
    n = int(sys.stdin.readline())
    x1, y1 = map(int, sys.stdin.readline().split())
    graph = []
    
    for i in range(n) :
        x, y = map(int, sys.stdin.readline().split())
        graph.append((x, y))
        
    x2, y2 = map(int, sys.stdin.readline().split())
    
    visited = [0] * n
    
    bfs(x1, y1, x2, y2)   