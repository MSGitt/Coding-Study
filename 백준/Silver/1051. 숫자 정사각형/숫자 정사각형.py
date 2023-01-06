import sys 


n, m = map(int, sys.stdin.readline().split()) 
grid = [] 

a = min(n, m)
result = 0

for i in range(n) : 
    grid.append(list(sys.stdin.readline())) 
    
for i in range(n) :
    for j in range(m) : 
        for k in range(a) : 
            if (i + k) < n and (j + k) < m and grid[i][j] == grid[i][j + k] == grid[i + k][j] == grid[i+k][j+k] : 
                result = max(result, (k+1)*(k+1)) 
                
print(result)
                