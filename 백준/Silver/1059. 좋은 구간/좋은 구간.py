import sys 


l = int(sys.stdin.readline()) 
num = list(map(int, sys.stdin.readline().split()))
n = int(sys.stdin.readline()) 
num.sort()

if n in num :
    print(0) 
    
else : 
    minn = 0
    maxn = 0
    result = 0
    
    for i in num : 
        if i < n : 
            minn = i 
        
        if i > n : 
            maxn = i 
            break 
   
    for j in range(minn + 1 , maxn - 1) : 
        for k in range(j+1, maxn) : 
            if j <= n and k >= n : 
                result += 1 
                
    print(result)
    

