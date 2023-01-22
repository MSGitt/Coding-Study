import sys
from collections import defaultdict

n = int(sys.stdin.readline())

vacation = defaultdict(int)

for i in range(n) :
    
    a, b = map(int, sys.stdin.readline().split())
    
    for i in range(a, b+1) :
        vacation[i] += 1
        
number = list(sorted(vacation.items()))

before = number[0][0]
height = number[0][1]

count = 1
result = 0

for i in range(1, len(number)) :

    if number[i][0] - 1 == before : 
        count += 1
        height = max(height, number[i][1])

        before = number[i][0]

    else :
        result += count * height
        
        count, height = 1, 0       
        height = max(height, number[i][1])
        before = number[i][0]

result += count * height

print(result)