import sys
from collections import defaultdict

n = int(sys.stdin.readline())
hashmap = defaultdict(int)

for i in range(n) :
    files = input()
    k = files.split('.')
    
    hashmap[k[1]] += 1
    
result = sorted(hashmap.items())

for i in result :
    print(i[0], i[1])