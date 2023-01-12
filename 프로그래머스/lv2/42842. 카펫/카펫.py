import math

def solution(brown, yellow):
    
         
    for i in range(1, int(math.sqrt(yellow)) + 1) : 
        if yellow % i == 0 :
            if 2 * (yellow // i + i) == brown - 4 :
                return [yellow//i + 2, i + 2]
            
#     total = brown + yellow 
    
#     i = 3
    
#     while True :
        
#         if total % i == 0 :
#             row = total // i
#             col = i 
            
#             if (row - 2) * (col - 2) == yellow :
#                 return [row, col]
        
#         i += 1
        
    