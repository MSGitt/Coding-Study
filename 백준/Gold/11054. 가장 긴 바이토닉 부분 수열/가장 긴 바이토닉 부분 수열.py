import sys

n = int(sys.stdin.readline())

number = list(map(int, sys.stdin.readline().split()))
number1 = number[::-1]

dp1 = [0] * n
dp2 = [0] * n 

for i in range(n) :
    for j in range(n) :
        if number[i] > number[j] and dp1[i] < dp1[j] :
            dp1[i] = dp1[j]        
        
        if number1[i] > number1[j] and dp2[i] < dp2[j] :
            dp2[i] = dp2[j]
            
    dp1[i] += 1
    dp2[i] += 1
        
dp2 = dp2[::-1]
result = 0

for i in range(n):
    result = max(result, dp1[i] + dp2[i] -1) 

print(result)