import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

k = n ** 2

matrix = [[0] * n for i in range(n)]

j = 0
temp = 0

while k > 0 :
    
    if temp == 0 :
        for i in range(j, n - j) :
            matrix[i][j] = k
            k -= 1
            
        temp = 1
        j += 1
                
    if temp == 1 :
        for i in range(j, n - j) :
            matrix[n - j][i] = k
            k -= 1
            
        temp = 2
                
    if temp == 2 :
        for i in range(n - j, j - 1, -1) :
            matrix[i][n - j] = k
            k -= 1
            
        temp = 3
                   
    if temp == 3 :
        for i in range(n - j, j - 1, -1) :
            matrix[j - 1][i] = k
            k -= 1
            
        temp = 0       

x, y = 0, 0

for i in range(len(matrix)) :
    print(*matrix[i])

    if m in matrix[i] :
        x, y = i, matrix[i].index(m)

print(x+1, y+1)              