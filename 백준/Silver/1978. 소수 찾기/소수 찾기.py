n = int(input())
number = map(int, input().split()) 
a = 0 

for i in number :     
    if i == 1 :
        a += 1 
        
    if i > 1 :
        
        for j in range(2, i) : 
            if i % j == 0 : 
                a += 1 
                break
                
            
print(n - a)