import sys 

n, k = map(int, sys.stdin.readline().split()) 
country = []

for i in range(1, n+1) :
    country.append(list(map(int, input().split())))
    
country.sort(key = lambda x : (x[1], x[2], x[3]), reverse = True) 

for i in range(n) : 
    if country[i][0] == k :
        result = i 
        
for i in range(n) : 
    if country[result][1:] == country[i][1:] : 
        print(i + 1)
        break 
        
        
    
