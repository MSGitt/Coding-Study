import sys 

n = int(sys.stdin.readline()) 
num1 = list(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline()) 
num2 = list(map(int, sys.stdin.readline().split()))

result = [] 
dict1 = {}

for i in num1 : 
    dict1[i] = 0 
    
for j in num2 : 
    if j not in dict1 : 
        print(0, end= " ")
    else : 
        print(1, end= " ")
    
        