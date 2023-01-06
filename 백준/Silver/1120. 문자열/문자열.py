import sys 


a, b = sys.stdin.readline().rstrip().split() 

result = 0
result1 = 50

if len(a) == len(b) :
    for i in range(len(a)) :
        if a[i] != b[i] :
            result += 1
            
    print(result) 
    
    
else : 
    for j in range(len(b)-len(a) + 1) :
        k = b[j : j + len(a)]
        
        for l in range(len(a)) :
            if a[l] != k[l] :
                result += 1 
                
        result1 = min(result1, result)
        result = 0
        
    print(result1)
                
                
        
    