import sys

n = int(sys.stdin.readline())

matrix = [list(sys.stdin.readline().rstrip()) for i in range(n)]

number = [list(sys.stdin.readline().rstrip()) for i in range(n)]

row = [1, -1, 0, 0, -1, -1, 1, 1]
col = [0, 0, 1, -1, -1, 1, -1, 1]

flag = 0

for i in range(n) :
    for j in range(n) :
        if number[i][j] == 'x' :
            if matrix[i][j] == '*' :
                flag = 1                                
            else :                                      
                count = 0
                for k in range(8) :
                    newx = i + row[k]
                    newy = j + col[k]
                    if 0 <= newx < n and 0 <= newy < n and matrix[newx][newy] == '*' :
                        count += 1
                    
                number[i][j] = count
                matrix[i][j] = count   

if flag == 1 :    
    for i in matrix :
        print(*i, sep = '')

else :
    for i in number :
        print(*i, sep = '')