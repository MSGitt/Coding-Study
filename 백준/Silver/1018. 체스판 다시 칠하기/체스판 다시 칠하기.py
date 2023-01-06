import sys


n, m = map(int, sys.stdin.readline().split())

a = []
b = []

for i in range(n) : 
    
    a.append(input())
    
for i in range(n - 7) :
    for j in range(m - 7) :
        
        idx1 = 0
        idx2 = 0
        
        for k in range(i, i+8) :
            for l in range(j, j+8) :
                if (k + l) % 2 == 0 : 
                    if a[k][l] != 'W': 
                        idx1 += 1  
                    if a[k][l] != 'B': 
                        idx2 += 1
                else :
                    if a[k][l] != 'B': 
                        idx1 += 1
                    if a[k][l] != 'W': 
                        idx2 += 1
                        
        b.append(idx1)
        b.append(idx2)
        
        
print(min(b))