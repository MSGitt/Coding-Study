import sys

matrix = [list(map(int, sys.stdin.readline().split())) for i in range(5)]

def find() :
    
    count = 0    
    temp3, temp4 = 0, 0
    
    for i in range(5) :
        temp1, temp2 = 0, 0      
        for j in range(5) :  
            if matrix[i][j] == 0 :
                temp1 += 1
                
            if matrix[j][i] == 0 :
                temp2 += 1

            if i == j :
                if matrix[i][j] == 0 :
                    temp3 += 1
                    
                if matrix[i][4-j] == 0 :
                    temp4 += 1
                    
        if temp1 == 5 :
            count += 1        
                       
        if temp2 == 5 :
            count += 1    
                    
        if temp3 == 5 :
            count += 1
            
        if temp4 == 5 :
            count += 1
            
    return count    
    
count = 0

for i in range(5) :
    ans = 0
    number = list(map(int, sys.stdin.readline().split()))
    
    for i in number :
        count += 1
        for j in range(5) :
            for k in range(5) :
                if matrix[j][k] == i :
                    matrix[j][k] = 0
                    ans = find()
                    
                if ans >= 3 :
                    print(count)
                    sys.exit()    