import sys
from itertools import combinations

n, s = map(int, sys.stdin.readline().split())

number = list(map(int, sys.stdin.readline().split()))

num1 = number[: n//2]
num2 = number[n//2 :]

sub_num1 = []
sub_num2 = []

for i in range(len(num1) + 1) :   
    a = combinations(num1, i)
    for j in a :
        sub_num1.append(sum(j))

for i in range(len(num2) + 1) :   
    a = combinations(num2, i)
    for j in a :
        sub_num2.append(sum(j))    
        
sub_num1.sort()
sub_num2.sort()

left = 0
right = len(sub_num2) - 1
result = 0

while left < len(sub_num1) and right >= 0 :
    
    temp = sub_num1[left] + sub_num2[right] 
    count1, count2 = 0, 0
    
    if temp == s :
        count1 += 1
        count2 += 1
        
        sub_left = left
        sub_right = right 
        
        left += 1
        right -= 1
        
        while left < len(sub_num1) and sub_num1[left] == sub_num1[sub_left] :
            count1 += 1
            left += 1
            
        while right >= 0 and sub_num2[right] == sub_num2[sub_right] :
            count2 += 1
            right -= 1
            
        result += count1 * count2
        
    elif temp < s :
        left += 1
        
    else :
        right -= 1
        
if s == 0 :
    result -= 1
    
print(result)     