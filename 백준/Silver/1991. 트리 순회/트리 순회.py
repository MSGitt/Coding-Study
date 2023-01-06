import sys

n = int(sys.stdin.readline())

tree = {}

for i in range(n) :
    
    root, left, right = map(str, sys.stdin.readline().split())
    tree[root] = (left, right)
    
def pre(root, tree) :
    
    if root == "." :
        return 
    
    print(root, end = "")
    pre(tree[root][0], tree)
    pre(tree[root][1], tree)
    
def ino(root, tree) :
    
    if root == "." :
        return 
    
    ino(tree[root][0], tree)
    print(root, end = "")
    ino(tree[root][1], tree)
    
    
def pos(root, tree) :
    
    if root == "." :
        return 
    
    pos(tree[root][0], tree)
    pos(tree[root][1], tree)
    print(root, end = "")
    
pre('A', tree)
print()
ino('A', tree)
print()
pos('A', tree)