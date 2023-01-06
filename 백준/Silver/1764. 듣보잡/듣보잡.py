import sys


n, m = map(int, sys.stdin.readline().split())

a = [sys.stdin.readline().rstrip() for i in range(n)]
b = [sys.stdin.readline().rstrip() for j in range(m)] 




common = set(a).intersection(b) 

common = sorted(list(common))

print(len(common))

for i in common :
    print(i)


