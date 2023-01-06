import sys


n = int(sys.stdin.readline())


for i in range(n) :
    
    stack = []
    flag = 1
    
    word = sys.stdin.readline().rstrip()
    
    for i in word :
        if i == "(" :
            stack.append(i)
            
        elif i == ")" and stack :
            stack.pop() 
            
        else :
            flag = 0
                   
    if not stack and flag : 
        print("YES")
        
    else :
        print("NO")