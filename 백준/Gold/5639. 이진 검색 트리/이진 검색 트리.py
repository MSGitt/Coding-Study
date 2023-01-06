import sys
sys.setrecursionlimit(10**9)

matrix = []

while True : 
    try :
        matrix.append(int(sys.stdin.readline()))
        
    except :
        break
        
def find(start, end, matrix) :
    
    if start > end : 
        return 
    
    root = matrix[start]
    idx = start + 1 
    
    while idx <= end :
        if matrix[idx] > root :
            break
            
        idx += 1
        
    find(start + 1, idx - 1, matrix)
    find(idx, end, matrix)
    
    print(root)
    
find(0, len(matrix) - 1, matrix)