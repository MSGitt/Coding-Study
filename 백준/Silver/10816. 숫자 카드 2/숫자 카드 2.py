import sys
import collections

n = int(sys.stdin.readline())

number1 = list(map(int, sys.stdin.readline().split()))
number1 = collections.Counter(number1)

m = int(sys.stdin.readline())

number2 = list(map(int, sys.stdin.readline().split())) 
result =[]

for i in number2 :
    if i in number1 : 
        result.append(number1[i])
        
    else :
        result.append(0)
        
print(*result)