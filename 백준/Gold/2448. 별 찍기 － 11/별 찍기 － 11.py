import sys

n = int(sys.stdin.readline())

graph = [[" "] * (2*n) for i in range(n)]

def draw(x, y, k) :
    
    if k == 3 :
        graph[x][y] = "*"
        graph[x+1][y-1] = graph[x+1][y+1] = "*"
        for i in range(-2, 3) :
            graph[x+2][y+i] = "*"
            
    else : 
        k //= 2 
        draw(x, y, k)
        draw(x + k, y - k, k)
        draw(x + k, y + k, k)
        
draw(0, n - 1, n)

for i in graph :
    print("".join(i))