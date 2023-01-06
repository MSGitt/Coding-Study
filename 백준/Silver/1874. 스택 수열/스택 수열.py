import sys

n = int(sys.stdin.readline())

stack = []
result = []
cur = 1
fl = 0

for i in range(n) :
    
    number = int(sys.stdin.readline())
    
    while cur <= number :
        
        stack.append(cur)
        result.append('+')
        
        cur += 1
        
    if stack[-1] == number :
        
        stack.pop()
        result.append('-')
        
    else : 
        print('NO')
        fl = 1
        break
        
if fl == 0:
    for i in result :
        print(i)
        