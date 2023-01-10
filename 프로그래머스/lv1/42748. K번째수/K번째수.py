def solution(array, commands):
    
    result = []
    
    for i in commands :
        if i[0] == i[1] :
             result.append(array[i[0]-1])
        
        else : 
            k = sorted(array[i[0]-1 : i[1]])
            result.append(k[i[2] - 1])
            
    return result
    
    