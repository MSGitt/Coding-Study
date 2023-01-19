import sys

n = int(sys.stdin.readline())
number = list(map(int, sys.stdin.readline().split()))

number.sort()

num = 3000000001 
result = []

if n == 3 :
    print(*number)
    sys.exit()

else : 
    for i in range(n - 2) : 
        temp = number[i]
        left = i + 1
        right = n - 1
    
        while left < right :
            temp_sum = temp + number[left] + number[right]
            if abs(temp_sum) <= abs(num) :
                result = [temp, number[left], number[right]]
                num = temp_sum
            
            if temp_sum < 0 :
                left += 1
            
            elif temp_sum > 0 :
                right -= 1
                
            else : 
                print(*result)
                sys.exit()
            
print(*result)