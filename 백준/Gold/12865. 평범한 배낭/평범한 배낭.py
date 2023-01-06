import sys

n, m = map(int, sys.stdin.readline().split())

bag = [[0] * (m + 1) for i in range(n)]
item = []

for i in range(n) :
    
    item.append(list(map(int, sys.stdin.readline().split())))
       
for i in range(n) :
    for j in range(m+1) :
        if i == 0 :
            if item[i][0] <= j :
                bag[i][j] = item[i][1]
                
        else :
            if j - item[i][0] < 0 :
                bag[i][j] = bag[i-1][j]
                
            else  :
                bag[i][j] = max(bag[i-1][j-item[i][0]] + item[i][1], bag[i-1][j])
                
print(bag[n-1][m])
    