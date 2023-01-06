import sys 

m = int(sys.stdin.readline())
number = []

for i in range(m) : 
    temp = sys.stdin.readline().strip().split() 
    
    if len(temp) == 1 : 
        if temp[0] == "all" : 
            number = [i for i in range(1, 21)]
            
        else : 
            number = []
    
    if temp[0] == "add" : 
        if int(temp[1]) not in number :
            number.append(int(temp[1]))
            
    if temp[0] == "remove" : 
        if int(temp[1]) in number :
            number.remove(int(temp[1]))
            
    if temp[0] == "check" : 
        if int(temp[1]) in number : 
            print(1) 
            
        else : 
            print(0) 
            
    if temp[0] == "toggle" :
        if int(temp[1]) in number : 
            number.remove(int(temp[1])) 
            
        else : 
            number.append(int(temp[1]))
            
   
            
        