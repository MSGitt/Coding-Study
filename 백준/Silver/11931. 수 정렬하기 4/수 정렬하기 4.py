import sys 

n = int(sys.stdin.readline()) 
dict = {} 

for i in range(n) : 
    dict[i] = int(sys.stdin.readline()) 

sorted_dict = sorted(dict.items(), key = lambda x : x[1], reverse = True) 

for i in sorted_dict : 
    print(i[1])