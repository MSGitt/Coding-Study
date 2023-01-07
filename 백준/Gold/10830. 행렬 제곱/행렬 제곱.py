import sys

n, k = map(int, sys.stdin.readline().split())

matrix = [list(map(int, sys.stdin.readline().split())) for i in range(n)]

def mul(matrix1, matrix2) :
     
    result = [[0] * n for i in range(n)]
    
    for i in range(n) :
        for j in range(n) :
            for k in range(n) :
                result[i][j] += matrix1[i][k] * matrix2[k][j]
                
            result[i][j] %= 1000
        
    return result

def cal(matrix, k) :
    
    if k == 1 :
        for i in range(n):
            for j in range(n):
                matrix[i][j] %= 1000
                
        return matrix
    
    num = cal(matrix, k // 2)
    
    if k % 2 == 0 :
        return mul(num, num)
    
    else :
        return mul(mul(num, num), matrix)
    
result = cal(matrix, k)

for i in result :
    print(*i)