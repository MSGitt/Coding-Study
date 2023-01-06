import sys 

n = int(sys.stdin.readline())

number = [64, 32, 16, 8, 4, 2, 1]
count = 0 

while n : 
    for i in number : 
        if i <= n : 
            n -= i 
            count += 1 
            
print(count)
    