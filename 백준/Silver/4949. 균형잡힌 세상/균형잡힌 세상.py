import sys




while True :
    
    word = sys.stdin.readline().rstrip()
    
    stack = []
    flag = 1
    
    if word == "." :
        break
        
    for i in word :
        if i == "[" or i == "(" :
            stack.append(i) 
            
            
        elif i == "]" :
            if len(stack) != 0 and stack[-1] == "[" :
                stack.pop() 
                
            else :
                flag = 0
                break
                
        elif i == ")" :
            if len(stack) != 0 and stack[-1] == "(" :
                stack.pop() 
             
            else :
                flag = 0
                break 
                
    if flag and not stack :
        print("yes")
        
    else :
        print("no")
            