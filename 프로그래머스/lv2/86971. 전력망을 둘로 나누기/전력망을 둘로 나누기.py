from collections import defaultdict, deque

def bfs(x, stop, n, matrix) : 
    
    visited = [0] * (n + 1)
    queue = deque()
    
    queue.append(x)
    visited[x] = 1
    
    count = 1
    
    while queue :
        a = queue.popleft()
        
        for i in matrix[a] : 
            if i == stop :
                continue 
                
            if visited[i] == 0 :
                count += 1
                queue.append(i)
                visited[i] = 1 
                
    return count

def solution(n, wires):
    
    matrix = defaultdict(set)
    
    for wire in wires:
        matrix[wire[0]].add(wire[1])
        matrix[wire[1]].add(wire[0])
        
    answer = n
        
    for wire in wires:
        v1 = wire[0]
        v2 = wire[1]
        diff = abs(bfs(v1, v2, n, matrix) - bfs(v2, v1, n, matrix))
        answer = min(diff, answer)

    return answer