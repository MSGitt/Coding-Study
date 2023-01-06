import sys 


a , b = map(int, sys.stdin.readline().split()) 
people = [i for i in range(1, a+1)] 
remove = []  

delete = b-1
while people : 
    remove.append(people.pop(delete)) 
    
    if people : 
        delete = (delete - 1 + b ) % len(people) 
        
print("<{}>".format(", ".join(map(str, remove))))
        
    
    


