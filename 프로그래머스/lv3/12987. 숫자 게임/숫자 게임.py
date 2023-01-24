import heapq

def solution(A, B):
    
    answer = 0
    
    A = [-i for i in A]
    B = [-i for i in B]
    
    heapq.heapify(A)
    heapq.heapify(B)
    
    while A and B :
        temp1 = -heapq.heappop(A)
        temp2 = -heapq.heappop(B)   
        
        if temp2 > temp1 :
            answer += 1
            
        else :
            heapq.heappush(B, -temp2)

    return answer