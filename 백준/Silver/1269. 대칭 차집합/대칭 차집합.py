import sys 


m, n = map(int, sys.stdin.readline().split()) 

num1 = set(map(int, sys.stdin.readline().split()))
num2 = set(map(int, sys.stdin.readline().split())) 

conj = len(num1 & num2) 

print(len(num1)+ len(num2) - 2 * conj)


