import heapq

def solution(n, works):
    
    if sum(works) <= n :
        return 0
    
    answer = 0
    
    for i in range(len(works)) :
        works[i] = -works[i]
    
    heapq.heapify(works)
    
    for i in range(n) :
        temp = heapq.heappop(works)
        temp += 1        
        heapq.heappush(works, temp)
        
    for i in works :
        answer += i ** 2
        
    return answer