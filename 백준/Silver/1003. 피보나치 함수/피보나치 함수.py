zero = [1, 0]
one = [0, 1]

t = int(input()) 

for i in range(t) : 
  
    n = int(input()) 
    
    if n == 0 :
        print("1 0") 
        
    if n == 1 :
        print("0 1")
            
    if n >= 2 :
        for j in range(2, n+1) :
            zero.append(zero[j-1] + zero[j-2])
            one.append(one[j-1] + one[j-2])
            
        print("{} {}".format(zero[-1], one[-1]))
        
        zero = [1, 0]
        one = [0, 1]