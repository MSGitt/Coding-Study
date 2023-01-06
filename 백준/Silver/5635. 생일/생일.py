import sys 

n = int(sys.stdin.readline()) 
result = []

for i in range(n) : 
    result.append(list(sys.stdin.readline().split())) 
    
result.sort(key = lambda x : (int(x[3]), int(x[2]), int(x[1])))

print(result[-1][0])
print(result[0][0])
    