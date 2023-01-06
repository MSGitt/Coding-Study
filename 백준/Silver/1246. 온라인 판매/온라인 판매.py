import sys 



n, m = map(int, sys.stdin.readline().split()) 
money = []
result = []
for i in range(m) :
    money.append(int(sys.stdin.readline())) 
    
    
money.sort()

price = 0
total = 0

for i in range(m) : 
    number = min(m-i, n)
    
    if total < money[i] * number :
        price = money[i]
        total = money[i] * number
    
    
print(price, total)