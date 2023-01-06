import sys


n, m = map(int, sys.stdin.readline().split())

tree = list(map(int, sys.stdin.readline().split())) 

start = 0
end = max(tree)

while start <= end :
    
    i = (start + end) // 2
    result = 0
    
    for j in tree :
        if i < j :
            result += j - i 
                     
    if result >= m :
        start = i + 1 
         
    else : 
        end = i - 1
    
print(end)
    