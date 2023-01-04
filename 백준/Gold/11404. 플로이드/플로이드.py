import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

matrix = [[float('inf')] * (n + 1) for i in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            matrix[i][j] = 0

for i in range(m) :
    a, b, c = map(int, sys.stdin.readline().split())
    matrix[a][b] = min(c, matrix[a][b])
    
for i in range(1, n + 1):
    for j in range(1, n + 1):
        for k in range(1, n + 1):
            matrix[j][k] = min(matrix[j][k], matrix[j][i] + matrix[i][k])
            
            
for i in range(1, n + 1) :
    for j in range(1, n + 1) :
        if matrix[i][j] == float('inf') :
            print(0, end = " ")
        else :
            print(matrix[i][j], end = " ")
    print()
