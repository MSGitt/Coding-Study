import sys 


n = int(sys.stdin.readline()) 

result = 0

for i in range(1, n+1) : 
    if i < 100 : 
        result += 1 
       
    else : 
        num = str(i) 
        if int(num[0]) - int(num[1]) == int(num[1]) - int(num[2]) :
            result += 1 
            
            
print(result)
    
    

