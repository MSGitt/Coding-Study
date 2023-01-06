import sys 


n = int(sys.stdin.readline())

for i in range(n) :
    
    h, w, n = map(int, sys.stdin.readline().split())
    
    k = n % h
    l = n // h + 1
    
    if k == 0 :
        k = h
        l -= 1
    
    print(k*100 + l)