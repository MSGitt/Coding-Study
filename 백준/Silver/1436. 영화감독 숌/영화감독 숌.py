import sys 

n = int(sys.stdin.readline()) 

target = 666 

while True : 
    if "666" in str(target)  : 
        n -= 1 
        if n == 0 :
            break 
    target += 1 
    
print(target)