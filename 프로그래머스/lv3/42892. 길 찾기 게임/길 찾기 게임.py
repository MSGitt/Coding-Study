from collections import defaultdict
import sys

sys.setrecursionlimit(int(1e9)) 

def preorder(node, tree, result1) :
    
    result1.append(node)
    
    if tree[node][1] != -1 :
        preorder(tree[node][1], tree, result1)
        
    if tree[node][2] != -1 :
        preorder(tree[node][2], tree, result1)

    
def postorder(node, tree, result2) :
    
    if tree[node][1] != -1 :
        postorder(tree[node][1], tree, result2)
        
    if tree[node][2] != -1 :
        postorder(tree[node][2], tree, result2)
        
    result2.append(node)
    
    
def solution(nodeinfo):
    answer = [[]]
    
    nodes = [[nodeinfo[i][0], nodeinfo[i][1], i + 1] for i in range(len(nodeinfo))]
    tree = [[-1] * 3 for i in range(len(nodeinfo) + 1)]
    
    nodes.sort(key = lambda x : (-x[1], x[0]))
    
    for x, y, idx in nodes :
        tree[idx][0] = x
        curr = nodes[0][2]
        while True :
            if x > tree[curr][0] :
                if tree[curr][2] == -1 :
                    tree[curr][2] = idx
                    break  
                curr = tree[curr][2]
                
            elif x < tree[curr][0] :
                if tree[curr][1] == -1 :
                    tree[curr][1] = idx
                    break    
                curr = tree[curr][1]
                
            else :
                break
                
    result1 = []
    result2 = []
    
    preorder(nodes[0][2], tree, result1)
    postorder(nodes[0][2], tree, result2)
    
    return [result1, result2]
