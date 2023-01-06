import sys 


n, m = map(int, sys.stdin.readline().split())

number = list(map(int, sys.stdin.readline().split())) 

number.sort()

result = 0 
l = m

for i in range(n - 2) : 
    for j in range(i+1 , n-1) :
        for k in range(j+1, n):
            result = number[i] + number[j] + number[k] 
            
            if result <= m :
                k = m - result
                l = min(k, l)
                
print(m - l)
    

