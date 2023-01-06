import sys

n, m = map(int, sys.stdin.readline().split()) 
people = set(map(int, sys.stdin.readline().split()[1:]))

party = []

for i in range(m) :   
    party.append(set(map(int, input().split()[1:])))

for j in range(m) :  
    for i in party :
        if i & people :
            people = people.union(i)

result = 0

for k in party :
    if people & k :
        continue            
    result += 1
    
print(result)