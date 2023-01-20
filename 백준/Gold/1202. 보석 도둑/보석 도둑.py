import sys
import heapq

n, k = map(int, sys.stdin.readline().split())

number = []
bag = []

for i in range(n) :
    a, b = map(int, sys.stdin.readline().split())
    heapq.heappush(number, (a, b))
    
for i in range(k) :
    a = int(sys.stdin.readline())
    heapq.heappush(bag, a)
    
result = 0
temp = []

for i in range(k) :
    a = heapq.heappop(bag)
    
    while number and a >= number[0][0] :
        weight, value = heapq.heappop(number)
        heapq.heappush(temp, -value)
        
    if temp :
        result -= heapq.heappop(temp)
        
    elif not number :
        break
        
print(result)