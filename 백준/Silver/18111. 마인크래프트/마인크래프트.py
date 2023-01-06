import sys


n, m, b = map(int, sys.stdin.readline().split()) 
number = [list(map(int, sys.stdin.readline().split())) for i in range(n)]

max_time = 100000000
max_height = 0
    
for i in range(257) : 
    plus = 0
    minus = 0
    for j in range(n) :
        for k in range(m) :
            if number[j][k] < i :
                plus += (i - number[j][k])
                
            else  : 
                minus += (number[j][k] - i) 
                
    total = minus + b 
    
    if total < plus :
        continue
     
    time = 2 * minus + plus 
    
    if time <= max_time :
        max_time = time
        max_height = i 
    
print(max_time, max_height)

        
        
        
    