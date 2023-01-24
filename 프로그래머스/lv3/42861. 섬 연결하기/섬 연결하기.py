def find_parent(parent, x) :
    
    if parent[x] != x :
        parent[x] = find_parent(parent, parent[x])
        
    return parent[x]

def union(parent, a, b) :
    
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    
    if a < b:
        parent[b] = a
        
    else:
        parent[a] = b
    

def solution(n, costs):
    answer = 0
    
    parent = [0] * (n) 
    
    for i in range(n) :
        parent[i] = i
        
    costs.sort(key = lambda x : x[2])
    
    for i in costs :
        a, b, cost = i
        if find_parent(parent, a) != find_parent(parent, b) :
            union(parent, a, b)
            answer += cost
     
    return answer