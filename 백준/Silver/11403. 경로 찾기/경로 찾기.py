import sys


n = int(sys.stdin.readline())

matrix = [list(map(int, sys.stdin.readline().split())) for i in range(n)]

for i in range(n) :
    for j in range(n) :
        for k in range(n) :
            if matrix[j][i] and matrix[i][k] :
                matrix[j][k] = 1 
                
for i in matrix :
    print(*i)

            
    