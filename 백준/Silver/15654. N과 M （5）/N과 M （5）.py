import sys

n, m = map(int, sys.stdin.readline().split())

number = list(map(int, sys.stdin.readline().split()))
number.sort()

result = []

def find(number) :
    
    if len(result) == m :
        print(*result)
        return
    
    for i in number : 
        if i not in result :
            result.append(i)
            find(number)
            result.pop()
            
find(number)
        
        