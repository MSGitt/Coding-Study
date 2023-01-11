import heapq


def solution(scoville, K):
    
    heapq.heapify(scoville)
    count = 0 
    
    while scoville[0] < K :

        if len(scoville) == 1 and scoville[0] < K :
            return -1 
        
        temp = heapq.heappop(scoville) + 2 * heapq.heappop(scoville)
        heapq.heappush(scoville, temp)
        count += 1
        
    return count
        
        
        
            