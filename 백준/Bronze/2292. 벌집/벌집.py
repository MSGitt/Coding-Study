import sys


n = int(sys.stdin.readline())

i = 1

while True :
    
    result = 3*(i**2) - 3*i + 1
    
    if n <= result :
        print(i)
        break
        
    i += 1 