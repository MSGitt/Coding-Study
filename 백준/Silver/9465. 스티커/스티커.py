import sys

n = int(sys.stdin.readline())

for i in range(n) :
    
    m = int(sys.stdin.readline())
    
    number = [list(map(int, sys.stdin.readline().split())) for i in range(2)] 
    
    if m > 1 :
        number[0][1] += number[1][0]
        number[1][1] += number[0][0]
        
        for j in range(2, m) :
            number[0][j] += max(number[1][j-1], number[1][j-2])
            number[1][j] += max(number[0][j-1], number[0][j-2])
            
    print(max(number[0][-1], number[1][-1]))