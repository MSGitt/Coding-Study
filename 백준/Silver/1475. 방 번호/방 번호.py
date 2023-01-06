import sys 
import collections 

n = int(sys.stdin.readline())  
num1 = [int(i) for i in str(n)]

num = collections.Counter(num1) 
maxn = []

count = 0
count1 = 0

num6 = num[6] 
num9 = num[9] 

if num6 >= num9 : 
    a = num6 - num9 
    if a % 2 == 0 : 
        count = num9 + (a // 2) 
        
    else : 
        count = num9 + (a // 2) + 1  
        
else : 
    a = num9 - num6 
    if a % 2 == 0 : 
        count = num6 + (a // 2) 
        
    else : 
        count = num6 + (a // 2) + 1  

for k, v in num.items() : 
    if k != 9 and k != 6 and v == max(num.values()) : 
        count1 = v 
        
if count1 >= count : 
    print(count1) 
    
else : 
    print(count)
        
        

    
        





