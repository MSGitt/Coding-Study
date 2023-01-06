import sys


n = int(sys.stdin.readline())
result = set(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline()) 
number = list(map(int, sys.stdin.readline().split())) 

for i in number :
    
    if i in result : 
        print(1)
        
    else  :
        print(0)