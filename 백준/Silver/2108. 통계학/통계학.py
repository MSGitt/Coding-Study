import sys
import collections


n = int(sys.stdin.readline())

number = []

for i in range(n) :
    
    a = int(sys.stdin.readline())
    number.append(a)
    
number.sort()

hashmap = collections.Counter(number)
hashmap = sorted(hashmap.items(), key = lambda item : item[1], reverse = True)
    

print(round(sum(number)/n))
print(number[(n-1)//2])

if len(number) > 1 and hashmap[0][1] == hashmap[1][1] :
    print(hashmap[1][0])

else : 
    print(hashmap[0][0])
       
print(max(number) - min(number))