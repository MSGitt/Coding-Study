import sys

operation = sys.stdin.readline().rstrip()

stack = []
res = []

def pri(x) :
    
    if x == '*'  or x == '/':
        return 3
    
    elif x == '+' or x == '-' :
        return 4

    return sys.maxsize

           
for i in range(len(operation)) :
    
    if operation[i] == '(' :
        stack.append(operation[i])
        
    elif operation[i].isalpha() :
        res.append(operation[i])
        
    elif operation[i] == ')' :
        
        while stack and stack[-1] != '(' :
            res.append(stack.pop())

        if stack[-1] == '(' :
            stack.pop()
        
    else : 
        while stack and pri(operation[i]) >= pri(stack[-1]):
            res.append(stack.pop())       
        stack.append(operation[i])
        
while stack :
    res.append(stack.pop())

for i in res:
    print(i, end='')