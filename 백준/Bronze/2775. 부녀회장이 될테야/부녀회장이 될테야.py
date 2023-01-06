import sys

n = int(sys.stdin.readline())

for i in range(n) :
    
    floor = int(sys.stdin.readline())
    num = int(sys.stdin.readline()) 
    
    people = [i for i in range(1, num + 1)] 
    
    for i in range(floor) :
        for j in range(1, num) :
            people[j] += people[j-1]
            
    print(people[-1])
    
    