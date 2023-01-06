import sys


n = int(sys.stdin.readline())

stack = []

for i in range(n) :
    
    com = sys.stdin.readline().split()
    
    if com[0] == 'push' :
        stack.append(com[1])
        
    elif com[0] == 'pop' :
        if stack :
            a = stack.pop()
            print(a)
            
        else : 
            print(-1)
            
    elif com[0] == 'size' :
        print(len(stack))
        
        
    elif com[0] == 'empty' :
        if stack : 
            print(0)
            
        else :
            print(1)
            
    elif com[0] == 'top' :
        if stack :
            print(stack[-1])
            
        else :
            print(-1)