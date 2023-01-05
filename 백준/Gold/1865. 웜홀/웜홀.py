import sys

n = int(sys.stdin.readline())

def bellman(x, road, a) : 
    
    visited = [int(1e9)] * (a + 1)
    
    visited[x] = 0
    
    for i in range(a) :
        for j in range(1, a + 1) :
            for new_p, new_w in road[j] : 
                if visited[new_p] > visited[j] + new_w :
                    if i == a - 1 :
                        return True
                    visited[new_p] = visited[j] + new_w
    
    return False 

for i in range(n) :
    
    a, b, c = map(int, sys.stdin.readline().split())
    road = [[] for i in range(a + 1)]
    
    for i in range(b) :
        s, p, w = map(int, sys.stdin.readline().split())
        road[s].append((p, w))
        road[p].append((s, w))
        
    for j in range(c) : 
        s, p, w = map(int, sys.stdin.readline().split())
        road[s].append((p, -w))
        
    result = bellman(1, road, a)
    
    if result : 
        print("YES")
    
    else :
        print("NO")