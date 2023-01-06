import sys
import collections

n = int(sys.stdin.readline())

for i in range(n) :
    
    types = []
    count = 1
    
    m = int(sys.stdin.readline())
    
    for i in range(m) :
        a, b = map(str, sys.stdin.readline().split())
        types.append(b) 
        
    b = collections.Counter(types) 
    
    for key in b.keys() :
        count *= (b[key] + 1)
        
    print(count - 1)
    