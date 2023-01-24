import math

def solution(n, stations, w):
    answer = 0
    
    temp = []
    
    for i in range(1, len(stations)) :
        temp.append((stations[i]-w-1) - (stations[i-1]+w))
        
    temp.append(stations[0]-w-1)
    temp.append(n-(stations[-1]+w))
    
    for i in temp :
        if i <= 0 :
            continue
            
        else :
            answer += math.ceil(i / (2 * w + 1))

    return answer