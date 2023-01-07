import sys

a = sys.stdin.readline().rstrip()
b = sys.stdin.readline().rstrip()

stack = []

for i in a :
    stack.append(i)    
    if i == b[-1] and ''.join(stack[-len(b):]) == b :
        for j in range(len(b)) :
            stack.pop()
       
if not stack :
    print('FRULA')
else :
    print(''.join(stack))