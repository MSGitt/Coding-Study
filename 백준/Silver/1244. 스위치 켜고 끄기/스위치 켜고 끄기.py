import sys 


n = int(sys.stdin.readline()) 
num = list(map(int, sys.stdin.readline().split())) 
stu = int(sys.stdin.readline()) 


for i in range(stu) :
    a, b = map(int, sys.stdin.readline().split())
    
    if a == 1 :
        for i in range(len(num)) :
            if (i+1) % b == 0 :
                num[i] = int(not num[i])
                
    else :
        for j in range(len(num)) :
            if (j+1) == b :
                front = j - 1 
                back = j + 1
                num[j] = int(not num[j]) 
                
                while True : 
                    if front >=0 and back <= len(num) - 1   :
                        if num[front] == num[back] :
                            num[front    ] = int(not num[front])
                            num[back] = int(not num[back])
                            
                        else : 
                            break 
                        
                    else : 
                        break
                    
                    front -= 1
                    back += 1 
            
k = 0
while k < len(num) : 
    print(num[k], end = " ") 
    if k % 20 == 19 : 
        print()
        
    k += 1 
        