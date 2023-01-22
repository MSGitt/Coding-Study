import sys
from collections import defaultdict
sys.setrecursionlimit(10**9)

n = int(sys.stdin.readline())
graph = defaultdict(list)

result = []
count = 0

for i in range(n) :
    
    a, b, c = map(int, sys.stdin.readline().split())   
    graph[a] = [b, c]
    
def inorder(node) :
    
    if graph[node][0] != -1 :
        inorder(graph[node][0])
        
    result.append(node)
    
    if graph[node][1] != -1 :
        inorder(graph[node][1])
    
def similar_inorder(node) :
    
    global count
    
    if graph[node][0] != -1 :
        similar_inorder(graph[node][0])
        count += 1
        
    if node == result[-1] :
        print(count)
        sys.exit()
        
    count += 1
    
    if graph[node][1] != -1 :
        similar_inorder(graph[node][1])
        count += 1

inorder(1)       
similar_inorder(1)   