from itertools import permutations

def solution(k, dungeons):

    n = len(dungeons)

    result = 0
    
    for i in permutations(dungeons, n) :
        
        energy = k
        count = 0

        for j in i :
            if energy < j[0] :
                continue 

            else :
                energy -= j[1]
                count += 1
        
        result = max(result, count)
    
    return result