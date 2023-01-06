n = list(map(int, input().split()))

result = n[2] - n[0] 
speed = result % (n[0] - n[1])

if speed == 0 : 
    print(result // (n[0]-n[1]) + 1) 
    
else : 
    print(result // (n[0]-n[1]) + 2)

        
      
    
    

