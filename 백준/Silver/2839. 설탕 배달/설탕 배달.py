import sys


n = int(sys.stdin.readline())

i = 0

if n % 5 == 0 :
    print(n // 5) 
      
else :
    while n > 0 :
        n -= 3
        i += 1
        
        if n % 5 == 0 :
            print(n // 5 + i)
            break 
            
        elif n < 3 and n > 0 :
            print(-1)
            break
            
        elif n == 0 :
            print(i)
            break
    