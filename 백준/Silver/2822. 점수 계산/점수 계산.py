import sys 

dict = {}
result = 0
index = []

for i in range(1, 9) : 
    dict[i] = int(sys.stdin.readline())
    
sorted_by_value = sorted(dict.items(), key=lambda x: x[1], reverse=True) 

for j in range(5) : 
    result += sorted_by_value[j][1]
    index.append(sorted_by_value[j][0])

index.sort() 

print(result)
print(*index)

