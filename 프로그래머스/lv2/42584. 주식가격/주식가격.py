from collections import deque

def solution(prices):
    
    answer = [0] * len(prices)
    queue = deque([(i, p) for i, p in enumerate(prices)])
    stack = []
    
    while queue :
        temp = queue.popleft()
        
        while stack and temp[1] < stack[-1][1] :
            k = stack.pop()
            answer[k[0]] = temp[0] - k[0]
            
        stack.append(temp)
                   
    while stack :
        k = stack.pop()
        answer[k[0]] = len(prices) - k[0] - 1
               
    return answer