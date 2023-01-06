import sys 


n = int(sys.stdin.readline()) 
mintime = 1001

for i in range(n) :
    
    a, b = map(int, sys.stdin.readline().split())  
    
    if a <= b :
         mintime = min(mintime, b)
            
print(mintime)
    
 

