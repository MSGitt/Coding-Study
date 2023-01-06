import sys
import heapq

n = int(sys.stdin.readline())

heap = []

for i in range(n) :
    
    k = int(sys.stdin.readline()) 
    
    if k == 0 :
        if not heap :
            print(0)
            
        else :    
            result = heapq.heappop(heap)
            print(-result) 
          
    else :
        heapq.heappush(heap, -k)