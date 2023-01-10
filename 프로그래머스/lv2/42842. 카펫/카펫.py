def solution(brown, yellow):
    
    total = brown + yellow 
    
    i = 3
    
    while True :
        
        if total % i == 0 :
            row = total // i
            col = i 
            
            if (row - 2) * (col - 2) == yellow :
                return [row, col]
        
        i += 1
        
    