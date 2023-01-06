import sys

n = int(sys.stdin.readline())

matrix = [list(map(int, sys.stdin.readline().split())) for i in range(n)] 

dic = {-1 : 0, 0 : 0, 1 : 0}

def div(x, y, matrix, n, dic) :
    
    number = matrix[x][y]
    
    for i in range(x, x + n) :
        for j in range(y, y + n) :
            if matrix[i][j] != number :
                n //= 3
                div(x, y, matrix, n, dic) 
                div(x, y + n, matrix, n, dic) 
                div(x, y + 2*n, matrix, n, dic) 
                div(x + n, y, matrix, n, dic) 
                div(x + 2*n, y, matrix, n, dic) 
                div(x + n, y + n, matrix, n, dic) 
                div(x + 2*n, y + n, matrix, n, dic) 
                div(x + n, y + 2*n, matrix, n, dic) 
                div(x + 2*n, y + 2*n, matrix, n, dic) 
                return
                
    dic[number] += 1
    return
    
div(0, 0, matrix, n, dic)

for i in dic.values() :
    print(i)