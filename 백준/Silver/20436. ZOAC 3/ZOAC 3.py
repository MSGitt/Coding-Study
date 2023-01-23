import sys

s, r = sys.stdin.readline().rstrip().split()

word = sys.stdin.readline().strip()

left = ['qwert', 'asdfg', 'zxcv']
right = ['     yuiop', '     hjkl', '    bnm']

left = [list(i) for i in left] 
right = [list(i) for i in right]

xl, yl = 0, 0
xr, yr = 0, 0

for i in range(3) :
    if s in left[i] :
        temp1 = left[i].index(s)
        xl = i
        yl = temp1
        
    if r in right[i] :
        temp2 = right[i].index(r)
        xr = i
        yr = temp2
    
result = 0
        
for i in word :
    result += 1
    for j in range(3) :
        if i in left[j] :
            y = left[j].index(i)
            x = j
            result += abs(x - xl) + abs(y - yl) 
            xl, yl = x, y
            break
            
        if i in right[j] :
            y = right[j].index(i)
            x = j
            result += abs(x - xr) + abs(y - yr) 
            xr, yr = x, y
            break
            
print(result)    