import sys

n, m = map(int, sys.stdin.readline().split())
train = [0] * n

for i in range(m) :
    op = list(map(int, sys.stdin.readline().split()))
    
    if op[0] == 1 :
        tr = op[1] - 1
        ch = op[2] - 1
        
        train[tr] = train[tr] | 1 << ch
        
    elif op[0] == 2 :
        tr = op[1] - 1
        ch = op[2] - 1
        
        train[tr] = train[tr] & ~(1 << ch)
        
    elif op[0] == 3 :
        tr = op[1] - 1
        
        train[tr] = (train[tr] << 1) & ~(1 << 20)
        
    else : 
        tr = op[1] - 1
        
        train[tr] = train[tr] >> 1 
        
print(len(set(train)))