from collections import deque

def solution(bridge_length, weight, truck_weights):
  
    bridge = deque([0] * bridge_length) 
    truck_weights = deque(truck_weights)
    result = 0
    temp = 0
    
    while True :
        result += 1
        temp -= bridge.popleft()
        
        if truck_weights :
            if truck_weights[0] + temp <= weight :
                temp += truck_weights[0]
                bridge.append(truck_weights.popleft())
                  
            else : 
                bridge.append(0) 
                
        if not bridge :
            return result