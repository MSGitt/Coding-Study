import sys
from collections import deque

n = int(sys.stdin.readline())

def bfs(x, y, graph) :
    
    queue = deque()
    visited = [[0] * (w+2) for i in range(h+2)]
    row = [1, -1, 0, 0]
    col = [0, 0, 1, -1]
    
    queue.append((x, y))
    visited[x][y] = 1    
    count = 0
    
    while queue :
        a, b = queue.popleft()
        for i in range(4):
            newx = a + row[i]
            newy = b + col[i]
            if 0 <= newx < h + 2 and 0 <= newy < w + 2 :
                if not visited[newx][newy] :
                    if graph[newx][newy] == '.' :
                        visited[newx][newy] = 1
                        queue.append((newx, newy))
                        
                    elif graph[newx][newy].islower() :
                        queue = deque()
                        visited = [[0] * (w+2) for i in range(h+2)]
                        
                        door[ord(graph[newx][newy]) - ord('a')] = 1
                        graph[newx][newy] = '.'
                        queue.append((newx, newy))
                    
                    elif graph[newx][newy].isupper() :
                        if door[ord(graph[newx][newy]) - ord('A')] == 1 :
                            visited[newx][newy] = 1
                            graph[newx][newy] = '.'
                            queue.append((newx, newy))
                            
                    elif graph[newx][newy] == '$':
                            visited[newx][newy] = 1
                            count += 1
                            graph[newx][newy] = '.'
                            queue.append((newx, newy))
                        
    return count    
        
for i in range(n) :
    h, w = map(int, sys.stdin.readline().split())
    graph = [list(sys.stdin.readline().rstrip()) for i in range(h)]
    key = list(sys.stdin.readline().rstrip())
    door = [0] * 26
    
    for i in key:
        if i != '0':
            door[ord(i)- ord('a')] = 1
            
    for i in range(h):
        for j in range(w):
            if ord('A') <= ord(graph[i][j]) <= ord('Z'):
                if door[ord(graph[i][j]) - ord('A')]:
                    graph[i][j] = '.'
                    
    for i in graph :
        i.insert(0, '.')
        i.append('.')
    graph.insert(0, ['.'] * (w+2))
    graph.append(['.'] * (w+2))
    
    result = bfs(0, 0, graph)
    
    print(result)   