import sys

x, y, w, h = map(int, sys.stdin.readline().split())

a = abs(0-x)
b = abs(0-y)
c = abs(w-x)
d = abs(h-y)

print(min(a,b,c,d))