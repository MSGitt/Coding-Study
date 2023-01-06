
number = set(range(1, 10001)) 
newnumber = set() 

for i in range(1, 10001) : 
    
    for j in str(i) : 
        i += int(j)  
    newnumber.add(i) 
    
a = sorted(number - newnumber) 

for k in a :
    print(k)
        