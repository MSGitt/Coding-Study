import sys

n, s = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))

left, right = 0, 0
length = n + 1
result = 0

while True :
    if result >= s :
        length = min(length, right - left)
        result -= numbers[left]
        left += 1 
        
    elif right == n :
        break
        
    else : 
        result += numbers[right]
        right += 1
      
if length == n + 1 :
    print(0)
    
else :
    print(length)