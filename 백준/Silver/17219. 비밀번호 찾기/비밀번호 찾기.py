import sys

n, m = map(int, sys.stdin.readline().split())

hashmap = {}

for i in range(n) :
    
    j, k = map(str, sys.stdin.readline().split())
    
    hashmap[j] = k 
    
for i in range(m) :
    
    j = sys.stdin.readline().rstrip()
    print(hashmap[j])