import sys
sys.setrecursionlimit(10**6)

def dfs(x) :
    
    global count 
    visited[x] = 1
    
    a = graph[x]
    
    if not visited[a] :
        dfs(a)
        
    else :
        if a not in team :
            nxt = a
            while nxt != x :
                count += 1
                nxt = graph[nxt]            
            count += 1
            
    team.add(x)

t = int(sys.stdin.readline())

for i in range(t) :
    n = int(sys.stdin.readline())
   
    visited = [0] * (n + 1)  
    graph = [0] + list(map(int, sys.stdin.readline().split()))
    
    team = set()
    count = 0
        
    for j in range(1, n + 1) : 
        if visited[j] == 0 : 
            dfs(j)
                
    print(n - count)   