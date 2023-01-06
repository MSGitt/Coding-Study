import sys 

n, k = map(int, sys.stdin.readline().split()) 

s = list(map(int, sys.stdin.readline().split()))

s.sort() 

print(s[k-1])