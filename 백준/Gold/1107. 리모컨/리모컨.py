import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

if m == 0 :
    broke = []

else :
    broke = list(map(int, sys.stdin.readline().split()))
    
count = abs(100 - n)

for i in range(1000001) :
    for j in str(i) :
        if int(j) in broke :
            break        
    else :
        count = min(count, len(str(i)) + abs(i - n))
        
print(count)