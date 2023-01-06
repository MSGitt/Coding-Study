import sys 


k, s, n = map(str, sys.stdin.readline().split())  

move = { "R": (1, 0),
         "L": (-1, 0),
         "B": (0, -1),
         "T": (0, 1),
         "RT": (1, 1),
         "LT": (-1, 1),
         "RB": (1, -1),
         "LB": (-1, -1) } 


ck = ord(k[0]) - ord("A") 
rk = int(k[1]) 

cs = ord(s[0]) - ord("A")
rs = int(s[1]) 


for i in range(int(n)) : 
    a = str(sys.stdin.readline().strip()) 
    a1, a2 = move[a] 
    
    if ck + a1 > 7 or ck + a1 < 0 or rk + a2 > 8 or rk + a2 < 1 :
        continue 
        
    ck += a1
    rk += a2 
    
    if ck == cs and rk == rs :
        if cs + a1 > 7 or cs + a1 < 0 or rs + a2 > 8 or rs + a2 < 1 :
            
            ck -= a1
            rk -= a2
            continue 
            
        cs += a1 
        rs += a2 
        
print(chr(ord("A")+ck)+str(rk))
print(chr(ord("A")+cs)+str(rs))
   
    

