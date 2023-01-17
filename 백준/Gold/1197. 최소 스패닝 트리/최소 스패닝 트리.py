import sys

v, e = map(int, sys.stdin.readline().split())

root = [i for i in range(v + 1)]
matrix = []

for i in range(e):
    matrix.append(list(map(int, sys.stdin.readline().split())))
    
matrix.sort(key=lambda x : x[2])

def find(x):
    if x != root[x]:
        root[x] = find(root[x])
        
    return root[x]

result = 0

for a, b, c in matrix :
    root1 = find(a)
    root2 = find(b)
    
    if root1 != root2 :
        if root1 > root2 :
            root[root1] = root2
            
        else :
            root[root2] = root1
            
        result += c
        
print(result)