def rotate(matrix, d) :
    
    for i in range(d) :
        matrix = [[row[i] for row in matrix[::-1]] for i in range(len(matrix[0]))]
    
    return matrix

def check(matrix) :
    
    n = len(matrix) // 3
    
    for i in range(n) :
        for j in range(n) :
            if matrix[n + i][n + j] != 1 :
                return False
            
    return True

def solution(key, lock):
    answer = True
    
    n = len(lock)
    m = len(key)
    
    matrix = [[0] * (3 * n) for i in range(3 * n)]
    
    for i in range(n) :        
        for j in range(n) :
            matrix[n + i][n + j] = lock[i][j]
    
    for i in range(1, 2 * n) :
        for j in range(1, 2 * n) :
            for k in range(4) :
                keys = rotate(key, k)
                for x in range(m) :
                    for y in range(m) :
                        matrix[i + x][j + y] += keys[x][y]
                        
                if check(matrix) :
                    return True
                
                for x in range(m) :
                    for y in range(m) :
                        matrix[i + x][j + y] -= keys[x][y]      
     
    return False