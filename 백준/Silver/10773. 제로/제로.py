import sys

n = int(sys.stdin.readline())
stack = []


for i in range(n) :
    
    num = int(sys.stdin.readline())
    
    if num != 0 :
        stack.append(num)
        
    elif num == 0 :
        stack.pop()
        
        
print(sum(stack))