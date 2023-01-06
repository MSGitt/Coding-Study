import sys


n = int(sys.stdin.readline())
count = 1
number = []

for i in range(n) :
    
    a, b = map(int, sys.stdin.readline().split())
    number.append((a, b))
    
number.sort(key = lambda x : (x[1], x[0]))

first = number[0][1]
for i in range(1, n) :
    if first <= number[i][0] :
        count += 1 
        first = number[i][1]
        
print(count)
