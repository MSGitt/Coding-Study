import sys 


n, k = map(int, sys.stdin.readline().split())

num = [i for i in range(1, n+1)] 
result = []

i = k - 1

while True : 
    result.append(num[i]) 
    num.remove(num[i])
    if not num : 
        break 
        
    i = (i + k - 1) % len(num)
        
    
    
print('<'+", ".join(list(map(str, result))) + '>')
    