n = str(input())
a = [] 

for i in range(len(n)) : 
    a.append(int(n[i])) 
    
a.sort(reverse=True) 

for k in a :
    print(k, end="")