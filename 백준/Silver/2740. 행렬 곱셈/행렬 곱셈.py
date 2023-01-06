import sys 


A = []
B = [] 

n, m = map(int, sys.stdin.readline().split())
for i in range(n) : 
    A.append(list(map(int, sys.stdin.readline().split()))) 
    
m, k = map(int, sys.stdin.readline().split())
for j in range(m) : 
    B.append(list(map(int, sys.stdin.readline().split()))) 
    
C = [[0 for i in range(k)] for j in range(n)]

    
for a in range(n):
    for b in range(k):
        for c in range(m):
            C[a][b] += A[a][c] * B[c][b]

for d in C :
    print(*d)