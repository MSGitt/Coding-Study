import sys

n = int(sys.stdin.readline())

number = [list(map(int, sys.stdin.readline().rstrip())) for i in range(n)]

def div(x, y, number, n) :
    
    if n == 1 :
        print(number[x][y], end ="")
        return
        
    num = number[x][y]
    
    for i in range(x, x + n) :
        for j in range(y, y + n) :
            if num != number[i][j] :
                print("(", end = "")
                n //= 2
                div(x, y, number, n)
                div(x, y + n, number, n)
                div(x + n, y, number, n)
                div(x + n, y + n, number, n)
                print(")", end = "")
                return 
            
    print(number[x][y], end="")
    return 

div(0, 0, number, n)
    
    