import sys


n = int(sys.stdin.readline())

row = [0] * n
result = 0

def pos(x) :
    for i in range(x) :
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i) :
            return False
            
    return True

def queen(x) :
    
    global result
    
    if x == n :
        result += 1
        return 
        
    for i in range(n) :
        row[x] = i
        if pos(x) :
            queen(x + 1)
        
queen(0)
print(result)
    
      