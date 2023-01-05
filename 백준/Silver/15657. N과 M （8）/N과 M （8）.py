import sys

n, m = map(int, sys.stdin.readline().split())
number = list(map(int, sys.stdin.readline().split()))

number.sort()
result = [0]

def find(number) :
    
    if len(result) == m + 1 :
        print(*result[1:])
        return 
    
    for i in number :
        if i >= max(result) :
            result.append(i)
            find(number)
            result.pop()
                        
find(number)