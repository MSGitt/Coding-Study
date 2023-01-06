import sys 

n = int(sys.stdin.readline()) 
num = [i for i in range(1, n+1)]
result = []

while True :
    result.append(num.pop(0))
    
    if not num :
        break 
        
    num.append(num.pop(0)) 
    
print(*result)
        
        