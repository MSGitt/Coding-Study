import sys

n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))

even = 0

for i in num :
    if i % 2 == 0 :
        even += 1 

result1, result2 = 0, 0
        
for i in range(len(num)) : 
    if num[i] % 2 == 0 :
        result1 += i

    if num[i] % 2 == 1 :
        result2 += i

result1 -= (even * (even - 1)) // 2
result2 -= ((n - even) * (n - even - 1)) // 2
        
print(min(result1, result2))     