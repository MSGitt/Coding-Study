import heapq

def solution(operations):
    
    
    min_heap = []
    max_heap = []
    number = [0] * len(operations)
    
    for i in range(len(operations)) : 
        a, b = operations[i].split()
        if a == 'I' :
            heapq.heappush(min_heap, (int(b), i))
            heapq.heappush(max_heap, (-int(b), i))
            number[i] = 1
        
        else : 
            if b == '1' :
                while max_heap and number[max_heap[0][1]] == 0 :
                    heapq.heappop(max_heap)
                    
                if max_heap :
                    number[max_heap[0][1]] = 0
                    heapq.heappop(max_heap)
                    
            else : 
                while min_heap and number[min_heap[0][1]] == 0 :
                    heapq.heappop(min_heap)
                    
                if min_heap :
                    number[min_heap[0][1]] = 0
                    heapq.heappop(min_heap)
                    
    while max_heap and number[max_heap[0][1]] == 0 :
                    heapq.heappop(max_heap)
            
    while min_heap and number[min_heap[0][1]] == 0 :
                    heapq.heappop(min_heap)
            
            
    if not max_heap or not min_heap : 
        return [0, 0]
    
    else : 
        return [-max_heap[0][0], min_heap[0][0]]