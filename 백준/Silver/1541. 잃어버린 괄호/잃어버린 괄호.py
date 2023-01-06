import sys 


eq = sys.stdin.readline()

neweq = eq.split('-')
result = 0

if eq[0] == '-' :
    result -= sum(map(int, (neweq[0].split('+'))))
    
else : 
    result += sum(map(int, (neweq[0].split('+'))))
    
for i in range(1, len(neweq)) :
    result -= sum(map(int, (neweq[i].split('+')))) 
    
    
print(result)
