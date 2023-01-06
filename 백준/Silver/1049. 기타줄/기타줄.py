import sys


n, m = map(int, sys.stdin.readline().split()) 

result = 0
money1 = []
money2 = []

for i in range(m) : 
    temp = list(map(int, sys.stdin.readline().split()))
    
    money1.append(temp[0])
    money2.append(temp[1])
    
money1.sort()
money2.sort()

if money1[0] <= money2[0] * 6 :
    result = money1[0] * (n // 6) + money2[0] * (n % 6) 
    
    if money1[0] < money2[0] * (n % 6) :
        result = money1[0] * (n //6 + 1)
        
else : 
    result = money2[0] * n 
    
print(result)

    