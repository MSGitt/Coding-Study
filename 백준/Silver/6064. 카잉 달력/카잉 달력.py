import sys


n = int(sys.stdin.readline())


for i in range(n) :
    
    m, n, x, y = map(int, sys.stdin.readline().split())
    flag = 1

    while x <= m * n :
        
        if (x - y) % n == 0 :
            print(x)
            flag = 0
            break
            
        x += m
        
    if flag == 1 :
        print(-1)
    
    