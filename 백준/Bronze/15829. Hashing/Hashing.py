import sys 


n = int(sys.stdin.readline()) 

m = 1234567891
r = 31 

result = 0

alph = sys.stdin.readline()

for i in range(n) :
    
    num = ord(alph[i]) - 96
    
    result += num * (r ** i)
    
print(result % m)