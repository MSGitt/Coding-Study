import sys
from collections import deque


a, b = map(int, sys.stdin.readline().split())

number = [list(map(int, sys.stdin.readline().split())) for i in range(b)]
count = 0

for i in number :
    for j in i :
        if j == 1 :
            count += 1 
            
if count == (a * b) :
    print(0)
    sys.exit(0)

ans = deque()

for i in range(b) :
    for j in range(a) :
        if number[i][j] == 1:
            ans.append((i, j))

def bfs(ans, number, b, a) :
    
    row = [0, 0, 1, -1]
    col = [1, -1, 0, 0]
    
    while ans :
        x, y = ans.popleft()
        
        for i in range(4) :
            newx = x + row[i]
            newy = y + col[i]
            
            if 0 <= newx < b and 0 <= newy < a and number[newx][newy] == 0 :
                ans.append((newx, newy))
                number[newx][newy] = number[x][y] + 1 
                

bfs(ans, number, b, a)            
ans = 0
         
for i in number :
    for j in i :
        if j == 0 :
            print(-1)
            sys.exit(0)
            
    ans = max(ans, max(i))

print(ans - 1)
    