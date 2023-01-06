import sys


m, n = map(int, sys.stdin.readline().split())

a, b = m, n

while b != 0 :
    
    a %= b 
    a, b = b, a
    
    
print(a)
print( (m * n) // a )