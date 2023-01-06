import sys 


n = int(sys.stdin.readline()) 
num = list(map(int, sys.stdin.readline().split())) 

count = 0 

i = 0 
j = 1
count = 0

while i < len(num) :
    
    if num[i] == j : 
  
        j += 1 
    
    else : 
        count += 1 
        
        
    i += 1
    
print(count)
        