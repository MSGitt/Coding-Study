import sys


n, m = map(int, sys.stdin.readline().split())

matrix = [ []  for i in range(n + 1)]
visited = [0] * (n+1)

for i in range(m) :
    
    a, b = map(int, sys.stdin.readline().split())
    
    matrix[a].append(b)
    matrix[b].append(a)
    
    
def dfs(n, visited, matrix) :
    
    stack = [n]
    
    while stack :
        a = stack.pop()
        if not visited[a] :
            visited[a] = 1
            for w in matrix[a] :
                stack.append(w)  
                  
    return visited 

count = 0 

for i in range(1, n + 1) :
    if not visited[i] :
        dfs(i, visited, matrix)
        count += 1
        
print(count)




    
    