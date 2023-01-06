import sys 

n = int(sys.stdin.readline())

i = 1 
result = 0 

while result + i <= n : 
    result += i 
    i += 1 
    
print(i-1)