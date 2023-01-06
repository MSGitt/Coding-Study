import sys


n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

s = sys.stdin.readline().rstrip()


p = 'IOI' + 'OI' * (n - 1)
count = 0

for i in range(len(s) - len(p) + 1) :
    if s[i : i + len(p)] == p :
        count += 1 
        
print(count)