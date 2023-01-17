import sys

n = int(sys.stdin.readline())

x = []
y = []

for i in range(n) :
    a, b = map(int, sys.stdin.readline().split())
    
    x.append(a)
    y.append(b)
    
x.append(x[0])
y.append(y[0])

result = 0
for i in range(n) :
    result += (x[i]*y[i+1])-(x[i+1]*y[i])
    
print(round(abs(result)/2,1))