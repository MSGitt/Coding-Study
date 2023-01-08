import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())

def find(x, k) :
    
    if x == k :
        return 0, 1
    
    visited = [[0,0] for i in range(100001)]
    queue = deque()
    
    visited[x][0] = 0
    visited[x][1] = 1
    queue.append(x)
    
    while queue :
        a = queue.popleft()
             
        for i in (a - 1, a + 1, a * 2) :
            if 0 <= i <= 100000 :
                if visited[i][0] == 0 :
                    visited[i][0] = visited[a][0] + 1
                    visited[i][1] = visited[a][1]
                    queue.append(i)

                elif visited[i][0] == visited[a][0] + 1  :
                    visited[i][1] += visited[a][1]
    
    return visited[k][0], visited[k][1]

r1, r2 = find(n, k)

print(r1)
print(r2)