import sys

n = int(sys.stdin.readline())

matrix = [list(map(int, sys.stdin.readline().split())) for i in range(n)] 
white = 0
blue = 0

def div(x, y, N, matrix) :
    
    global white, blue
    
    color = matrix[x][y] 
    
    check = 1
    
    for i in range(x, x + N) :
        if not check :
            break 
            
        for j in range(y, y + N) :
            if color != matrix[i][j] :
                check = 0
                div(x, y,  N // 2, matrix)
                div(x + N // 2, y,  N // 2, matrix)
                div(x, y + N // 2,  N // 2, matrix)
                div(x + N // 2, y + N // 2, N // 2, matrix)
                break
                
    if check :
        
        if color == 0 :
            white += 1 
        
        else :
            blue += 1 


div(0, 0, n, matrix)

print(white)
print(blue)