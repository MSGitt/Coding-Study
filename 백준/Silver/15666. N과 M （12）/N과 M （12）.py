import sys

n, m = map(int, sys.stdin.readline().split())
number = list(map(int, sys.stdin.readline().split()))
number.sort()

result = [0]

def find(number) :
    
    if len(result) == m + 1 :
        print(*result[1:])
        return 
    
    last = 0   
    for i in range(len(number)) : 
        if number[i] >= max(result) and number[i] != last :
            result.append(number[i])
            last = number[i]
            
            find(number) 
            
            result.pop()
            
find(number)
