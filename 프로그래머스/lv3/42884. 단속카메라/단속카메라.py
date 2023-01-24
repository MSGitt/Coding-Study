def solution(routes):
    answer = 0
    
    routes.sort(key = lambda x : x[1])
    cam = -30001
    
    for i in routes : 
        if cam < i[0] :
            answer += 1
            cam = i[1]
    
    return answer