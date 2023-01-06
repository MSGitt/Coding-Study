import sys
import heapq

n = int(sys.stdin.readline()) 
result = [0] * 10000

for i in range(n) :
    
    number = int(sys.stdin.readline())
    result[number-1] += 1 
    
for i in range(10000) :
    
    if result[i] != 0 :
        
        for j in range(result[i]) :
            print(i+1)
    

