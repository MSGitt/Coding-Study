import sys



n = int(sys.stdin.readline())

def pro(n) :
    
    if n == 1 :
        return 1
    
    elif n == 2 :
        return 2
    
    elif n == 3:
        return 4
    
    return pro(n - 3) + pro(n - 2) + pro(n - 1)


for i in range(n) :
    
    m = int(sys.stdin.readline())
    
    result = pro(m)
    
    print(result)
    
    