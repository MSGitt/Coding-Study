import sys

n = int(sys.stdin.readline()) 
info = [] 

for i in range(n)  :
    info.append(list(sys.stdin.readline().split())) 
    
info.sort(key = lambda x : int(x[0])) 

for k in info : 
    print(k[0], k[1])
    