import sys

n = int(sys.stdin.readline())

number = list(map(int, sys.stdin.readline().split()))

number.sort() 

result = 0 

for i in range(n) :
    result += number[i] * (n - i)
    
print(result)