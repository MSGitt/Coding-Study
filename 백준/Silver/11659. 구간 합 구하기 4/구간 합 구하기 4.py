import sys

n, m = map(int, sys.stdin.readline().split())

number = list(map(int, sys.stdin.readline().split()))
num = 0

for i in range(len(number)) :
    
    num += number[i]
    number[i] = num

for i in range(m) :
    
    a, b = map(int, sys.stdin.readline().split())
    
    if a == b :
        if a == 1 :
            print(number[a-1])

        else :
            print(number[b-1] - number[b-2])
    
    elif a == 1 :
        print(number[b-1])
          
    else :
        print(number[b-1] - number[a-2])
    