import sys 


n = int(sys.stdin.readline()) 
hashmap = {} 

for i in range(n) :
    a = str(sys.stdin.readline().rstrip())
    hashmap[a] = hashmap.get(a, 0) + 1 
    
hashmap = sorted(hashmap.items(), key = lambda x : x[0] )
hashmap.sort(key = lambda x : x[1], reverse = True)

print(hashmap[0][0])


    