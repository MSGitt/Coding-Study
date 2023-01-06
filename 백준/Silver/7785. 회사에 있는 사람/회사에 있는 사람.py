import sys 

n = int(sys.stdin.readline()) 
dic = {}

for i in range(n) : 
    a, b = map(str, sys.stdin.readline().split())
    if b == "enter" : 
        dic[a] = 1  
        
    if b == "leave" : 
        del dic[a]
        

dic = sorted(dic.keys(), reverse = True)

for i in dic :
    print(i)