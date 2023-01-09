from collections import defaultdict

def solution(genres, plays):
    
    temp = []
    hashmap = defaultdict(int) 
    
    answer = []
    
    for i, k in enumerate(zip(genres, plays)) :
        temp.append((i, k[0], k[1]))
        hashmap[k[0]] += k[1]
        
    temp.sort(key = lambda item : -item[2])
    hashmap = sorted(hashmap.items(), key = lambda item : -item[1])
    
    for k, v in hashmap :
        count = 0
        for i in range(len(temp)) :
            if temp[i][1] == k :
                count += 1
                if count > 2 :
                    break
                else :
                    answer.append(temp[i][0])
                    
    return answer
         