import sys

n = int(sys.stdin.readline())
stock = list(map(int, sys.stdin.readline().split()))

first = n
first_count = 0

for i in stock :
    count = 0
    if i <= first :
        first_count += n // i
        first -= (n // i) * i 
        
second = n
second_count = 0

down_count = 0 
up_count = 0

for i in range(1, len(stock)) :
    before = stock[i-1]
    now = stock[i]
    
    if before > now :
        down_count += 1
        up_count = 0
        if down_count >= 3 :
            second_count += second // now
            second -= (second // now) * now
            
    if before < now :
        up_count += 1
        down_count = 0
        if up_count >= 3 :
            second += second_count * now
            second_count = 0
            
    if before == now :
        up_count = 0
        down_count = 0
        
r1 = first + first_count * stock[-1] 
r2 = second + second_count * stock[-1]

if r1 > r2 :
    print('BNP')
    
elif r1 < r2 :
    print('TIMING')
    
else :
    print('SAMESAME')    