from collections import defaultdict

def solution(clothes):
    
    hashmap = defaultdict(int)
    
    for i in clothes : 
        hashmap[i[1]] += 1
        
    result = 1
    
    for v in hashmap.values() :
        result *= (v + 1) 
        
    return result - 1
    