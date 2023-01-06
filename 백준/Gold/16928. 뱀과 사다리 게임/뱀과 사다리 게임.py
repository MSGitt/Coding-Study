import sys
from collections import deque 
from collections import defaultdict

m, n = map(int, sys.stdin.readline().split())

visited = [0] * 101
matrix = [0] * 101
move = defaultdict(int)

for i in range(m) :
    a, b = map(int, sys.stdin.readline().split())
    move[a] = b
    
for i in range(n) :
    a, b = map(int, sys.stdin.readline().split())
    move[a] = b
       
def bfs(x, matrix, visited, move) :
    
    queue = deque()
    
    queue.append(x)
    visited[x] = 1
    
    while queue :
        a = queue.popleft()
        
        if a == 100 :
            return matrix[a]
        
        for i in range(1, 7) :
            newmove = a + i
            
            if newmove <= 100 and visited[newmove] == 0 :
                if newmove in move.keys() :
                    newmove = move[newmove]
                    
                if visited[newmove] == 0 :
                    visited[newmove] = 1
                    matrix[newmove] = matrix[a] + 1
                    queue.append(newmove)
                
print(bfs(1, matrix, visited, move))