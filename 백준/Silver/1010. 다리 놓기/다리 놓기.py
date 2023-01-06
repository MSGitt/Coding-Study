import sys 

num = int(sys.stdin.readline()) 

def choose(n, k):
    numerator = 1
    denominator = 1
    k = min(n-k, k) 
    for i in range(1, k+1):
        denominator *= i
        numerator *= n+1-i
    return numerator//denominator

for i in range(num) : 
    a , b = map(int, sys.stdin.readline().split())
    print(choose(b, a))
    