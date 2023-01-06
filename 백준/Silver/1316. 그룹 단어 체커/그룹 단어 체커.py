n = int(input())

for i in range(n) : 
    eng = input() 
    for i in range(len(eng)-1) : 
        if eng[i] != eng[i+1] : 
            if eng[i] in eng[i+1:] :
                n -= 1 
                break 
                
print(n)
            
            
        