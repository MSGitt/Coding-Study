n = int(input()) 
inform = []
ranking =[]

for i in range(n) : 
    a, b = map(int, input().split()) 
    inform.append((a,b))
    
for j in range(n) : 
    rank = 1 
    for k in range(n) :
        if inform[j][0] < inform[k][0] and inform[j][1] < inform[k][1] : 
            rank += 1
    ranking.append(rank)
            
print(*ranking)
            
    