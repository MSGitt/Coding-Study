import sys
import copy

sudoku = [list(map(int, list(sys.stdin.readline().rstrip()))) for i in range(9)]

zeros = [(i,j) for i in range(9) for j in range(9) if not sudoku[i][j]]
number = [i for i in range(1,10)]

def backtrack(n) :
    
    if n == len(zeros) :
        for i in sudoku :
            print(*i,sep="")
            
        sys.exit()
        
    x, y = zeros[n]
    a, b = x//3, y//3
    number1 = copy.deepcopy(number)
    
    for i in range(3*a,(a+1)*3) :
        for j in range(3*b,(b+1)*3) :
            if sudoku[i][j] in number1 :
                number1.remove(sudoku[i][j])
                
    for i in range(9):
        if sudoku[x][i] in number1 :
            number1.remove(sudoku[x][i])
        if sudoku[i][y] in number1 :
            number1.remove(sudoku[i][y])
            
    for i in number1 :
        sudoku[x][y] = i
        backtrack(n+1)
        
    sudoku[x][y] = 0
    
backtrack(0)