import sys
import heapq

n = int(sys.stdin.readline())

for i in range(n) :
    
    heap1 = []
    heap2 = []
    
    m = int(sys.stdin.readline())
    number = [0] * m
    
    for j in range(m) :
        a, b = map(str, sys.stdin.readline().split())
        
        if a == 'I' :
            heapq.heappush(heap1, (int(b), j))
            heapq.heappush(heap2, (-int(b), j))
            number[j] = 1
        
        else : 
            if int(b) == 1 :
                while heap2 and number[heap2[0][1]] == 0 :
                    heapq.heappop(heap2)
                    
                if heap2 :
                    number[heap2[0][1]] = 0
                    heapq.heappop(heap2)
                    
            else :
                while heap1 and number[heap1[0][1]] == 0 :
                    heapq.heappop(heap1)
                    
                if heap1 :
                    number[heap1[0][1]] = 0
                    heapq.heappop(heap1)
                    
    while heap2 and number[heap2[0][1]] == 0 :
                    heapq.heappop(heap2)
            
    while heap1 and number[heap1[0][1]] == 0 :
                    heapq.heappop(heap1)
    
    if not heap1 or not heap2 :
        print("EMPTY")

    else :
        print("{} {}".format(-heap2[0][0], heap1[0][0]))