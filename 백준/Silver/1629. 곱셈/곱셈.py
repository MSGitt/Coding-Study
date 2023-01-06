import sys


a, b, c = map(int, sys.stdin.readline().split())

first = a % c

def div(a, b, c) :
    
    if b == 1 :
        return a % c
    
    num = div(a, b//2, c)
    
    if b % 2 == 0 :
        return (num*num) % c
    
    else : 
        return (num*num*a) % c
    
print(div(a, b, c))