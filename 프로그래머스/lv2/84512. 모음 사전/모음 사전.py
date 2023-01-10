from itertools import product

def solution(word):
    
    dictionary =  ['A', 'E', 'I', 'O', 'U']
    
    result = []

    for i in range(1, 6) :
        result += list(product(dictionary,  repeat = i)) 
        
    result = [''.join(i) for i in result]
    result.sort()
        
    return result.index(word) + 1
    