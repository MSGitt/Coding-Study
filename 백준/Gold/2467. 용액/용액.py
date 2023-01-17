import sys

n = int(sys.stdin.readline())
number = list(map(int, sys.stdin.readline().split()))

result = abs(number[0] + number[n-1])
left = 0
right = n - 1
ans1, ans2 = left, right

while left < right :
    
    temp = number[left] + number[right]
    
    if abs(temp) < result :
        ans1 = left
        ans2 = right
        result = abs(temp)
        
        if result == 0 :
            break
            
    if temp < 0 :
        left += 1
        
    else :
        right -= 1
        
print(number[ans1], number[ans2])