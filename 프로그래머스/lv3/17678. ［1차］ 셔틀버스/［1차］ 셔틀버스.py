def solution(n, t, m, timetable):
    
    temp1, temp2 = '', ''
    timetable.sort()
    
    shuttle = [540 + (t * i) for i in range(n)] 
    timetable = [60 * int(i[:2]) + int(i[3:]) for i in timetable]
    
    j = 0
    
    for i in shuttle :
        count = 0
        while count < m and j < len(timetable) and timetable[j] <= i :
            j += 1
            count += 1
            
        if count < m :
            answer = i 
            
        else :
            answer = timetable[j - 1] - 1
              
    temp1 = answer // 60
    temp2 = answer % 60
    
    return str(temp1).zfill(2) + ':' + str(temp2).zfill(2)