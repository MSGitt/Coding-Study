import sys 
import math

n, m, k = map(int, sys.stdin.readline().split()) 

a = math.comb(n, m) 
b = 0 

for i in range(0, k) : 
    b += math.comb(m, i) * math.comb(n-m, m-i) 
    
print((a-b)/a)