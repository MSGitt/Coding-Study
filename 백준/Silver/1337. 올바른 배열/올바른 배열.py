import sys 


n = int(sys.stdin.readline())
num = [] 

for i in range(n) :
    num.append(int(sys.stdin.readline())) 
    
num.sort() 

rresult = 5

for j in range(len(num)) : 
    result = 0
    
    for k in range(num[j], num[j] + 5) :
        if k not in num : 
            result += 1 
            
    rresult = min(rresult, result) 
    
    
print(rresult)

