import sys 


n = int(sys.stdin.readline()) 

num = list(map(int, sys.stdin.readline().split())) 

result = list(set(num)) 
result.sort() 

print(*result)