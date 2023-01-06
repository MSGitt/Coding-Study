import sys 

n = int(sys.stdin.readline()) 
stu = []

for i in range(n) : 
    stu.append(str(sys.stdin.readline().rstrip())) 

for k in range(1, len(stu[0]) + 1) :
    result = []
    
    for j in range(n) : 
        if stu[j][-k :] in result : 
            break 
            
        else : 
            result.append(stu[j][-k :])
    
    if len(result) == n :
        print(k)
        break