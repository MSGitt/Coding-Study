import sys 

n = int(sys.stdin.readline()) 

num = 1
count = 0 

for i in range(1, n+1) : 
    num *= i 
    
for i in range(len(str(num))) : 
    if str(num)[-1-i] == "0" : 
        count += 1 
        
    else : 
        break 
        
print(count)