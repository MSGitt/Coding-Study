from collections import deque, defaultdict

def dfs(matrix) :
    
    stack = deque()
    path = []

    stack.append('ICN')

    while stack :
        a = stack.pop()
        if a not in matrix or len(matrix[a]) == 0 :
            path.append(a)

        else : 
            stack.append(a)
            stack.append(matrix[a].pop(0))
    
    return path[::-1]
        
def solution(tickets):
   
    matrix = defaultdict(list)
    for i in tickets :
        matrix[i[0]].append(i[1])
        
    for i in matrix.keys() :
        matrix[i].sort()
        
    result = dfs(matrix)
    
    return result