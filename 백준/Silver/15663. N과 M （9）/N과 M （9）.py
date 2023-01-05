import sys

n, m = map(int, sys.stdin.readline().split())
number = list(map(int, sys.stdin.readline().split()))

number.sort()

result = []
visited = [0] * n

def find(number, visited) :
       
    if len(result) == m  : 
        print(*result)
        return
    
    last = 0
    
    for i in range(len(number)) :
        if visited[i] == 0 and number[i] != last :
            result.append(number[i])
            visited[i] = 1
            last = number[i]
            
            find(number, visited)

            result.pop()
            visited[i] = 0

find(number, visited)            
                         