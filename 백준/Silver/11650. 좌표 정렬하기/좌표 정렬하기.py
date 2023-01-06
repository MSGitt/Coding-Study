import sys
n = int(sys.stdin.readline())

coord = []
for i in range(n) : 
    a, b = map(int, sys.stdin.readline().split()) 
    coord.append((a,b)) 
    
coord.sort(key = lambda x : (x[0], x[1]))

for k in coord : 
    print(k[0], k[1])
