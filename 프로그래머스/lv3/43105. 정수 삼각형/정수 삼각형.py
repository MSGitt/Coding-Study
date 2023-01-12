def solution(triangle):
    
    n = len(triangle)
    
    for i in reversed(range(n-1)) :
        for j in range(len(triangle[i])) :
            triangle[i][j] += max(triangle[i+1][j], triangle[i+1][j + 1])    
    
    
    return triangle[0][0]