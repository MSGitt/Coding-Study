import sys


n, m = map(int, sys.stdin.readline().split())

hashmap1 = {}
hashmap2 = {}

for i in range(n) :
    
    name = sys.stdin.readline().rstrip()
    hashmap1[name] = i+1 
    hashmap2[i+1] = name
    
    
for i in range(m) :
    
    k = sys.stdin.readline().rstrip() 
    
    if k.isdigit() :
        print(hashmap2[int(k)])
                
    else :
        print(hashmap1[k])