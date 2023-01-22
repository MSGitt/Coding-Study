import sys

n = int(sys.stdin.readline())

def draw(n, i) :
    
    if n == 1 :
        matrix[i][i] = '*'
        return
    
    k = 4 * n - 3    
    
    for j in range(i, i + k) :
        matrix[i][j] = '*'
        matrix[i + k - 1][j] = '*'
        
        matrix[j][i] = '*'
        matrix[j][i + k - 1] = '*'
        
    return draw(n - 1, i + 2)


matrix = [[' '] * (4 * n - 3) for i in range(4 * n - 3)]

draw(n, 0)

for i in range(len(matrix)) :
    for j in range(len(matrix)) :
        print(matrix[i][j], end ='')
    print() 