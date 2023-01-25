def check(build) :
    
    for x, y, stuff in build :
        if stuff == 0 :
            if y == 0 or [x-1, y, 1] in build or [x, y, 1] in build or [x, y-1, 0] in build :
                continue
                
            return False
        
        elif stuff == 1 :
            if [x, y-1, 0] in build or [x+1, y-1, 0] in build or ([x-1, y, 1] in build and [x+1, y, 1] in build) : 
                continue 
                
            return False
        
    return True

def solution(n, build_frame):
    
    build = []
    
    for i in build_frame : 
        x, y, t, op = i 
        if op == 1 :
            build.append([x, y, t])
            if not check(build) :
                build.remove([x, y, t])
            
        elif op == 0 :
            build.remove([x, y, t])
            if not check(build) :
                build.append([x, y, t])
       
    build.sort()
    
    return build