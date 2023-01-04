import sys
sys.setrecursionlimit(10 ** 5)

n = int(sys.stdin.readline())

inorder = list(map(int, sys.stdin.readline().split()))
postorder = list(map(int, sys.stdin.readline().split()))

def find(i, j, x, y) :
    
    if i > j or x > y :
        return 
    
    root = postorder[y]
    
    left = inorder.index(root) - i
    right = j - inorder.index(root)
    
    print(root, end = " ")
    
    find(i, i + left - 1, x, x + left - 1)
    find(j - right + 1, j, y - right, y - 1)
    
find(0, n - 1, 0, n - 1)