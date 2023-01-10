import collections

def solution(participant, completion):
    
    p1 = collections.Counter(participant)
    p2 = collections.Counter(completion)

    for k, v in p1.items() :
        p1[k] -= p2[k] 

        if p1[k] == 1 :
            return k
    