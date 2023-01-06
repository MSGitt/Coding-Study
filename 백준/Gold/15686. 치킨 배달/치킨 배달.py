import sys
from itertools import combinations

n, m = map(int, sys.stdin.readline().split())
matrix = [list(map(int, input().split())) for i in range(n)]

chicken = []
house = []
result = 1000000

for i in range(n):
    for j in range(n):
        if matrix[i][j] == 1:
            house.append((i, j))
        elif matrix[i][j] == 2:
            chicken.append((i, j))
            
for i in combinations(chicken, m) :
    length = 0
    for j in house :
        chi_length = 1000
        for k in range(m) :
            chi_length = min(chi_length, abs(j[0] - i[k][0]) + abs(j[1] - i[k][1]))            
        length += chi_length       
    result = min(result, length)
    
print(result)