import sys 


n, m, k = map(int, sys.stdin.readline().split()) 

score = []

if n :
    score = list(map(int, sys.stdin.readline().split())) 
    score.append(m)
    score.sort(reverse = True) 
    rank = score.index(m) + 1 
    
    if rank > k :
        print(-1)
        
    else : 
        if n == k and m == score[-1] :
            print(-1) 
            
        else : 
            print(rank)

else :
    print(1)
