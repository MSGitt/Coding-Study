import sys


n = int(sys.stdin.readline())

number = []
dp = []

for i in range(n) :
    number.append(int(sys.stdin.readline()))
    

if n == 1:
    print(number[-1])

elif n == 2 :
    dp.append(max(number[0] + number[1] , number[1]))
    print(dp[-1])

else : 
    dp.append(number[0])
    dp.append(max(number[0] + number[1] , number[1]))
    dp.append(max(number[0] + number[2], number[1] + number[2]))

    for i in range(3, n) :
        dp.append(max(dp[i-2] + number[i], dp[i-3] + number[i-1] + number[i] )) 
    
    
    print(dp[-1])
    