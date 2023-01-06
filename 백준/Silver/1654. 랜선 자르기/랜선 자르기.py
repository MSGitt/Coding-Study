import sys


k, n = map(int, sys.stdin.readline().split())

arr = []


for i in range(k) :
    
    arr.append(int(sys.stdin.readline()))
    
    
first = 1
last = max(arr)
    
  
while first <= last :
    
    mid = (first + last) // 2 
    result = 0
    
    for i in range(k) :
        result += arr[i] // mid 
        
    if result >= n :
        first = mid + 1 
        
    else : 
        last = mid - 1 
        
print(last)