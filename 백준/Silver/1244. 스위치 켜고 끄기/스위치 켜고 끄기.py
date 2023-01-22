import sys

n = int(sys.stdin.readline())
switch = list(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline())

for i in range(m) :
    a, b = map(int, sys.stdin.readline().split())
    
    if a == 1 :
        for j in range(len(switch)) :
            if (j + 1) % b == 0 :
                switch[j] = abs(switch[j] - 1)
                
    if a == 2 :
        for j in range(len(switch)) :
            if (j + 1) == b :
                left = j - 1
                right = j + 1
                switch[j] = abs(switch[j] - 1)
                
                while left >= 0 and right < len(switch) :
                    if switch[left] == switch[right] :
                        switch[left] = abs(switch[left] - 1)
                        switch[right] = abs(switch[right] - 1)
                        
                    else :
                        break
                        
                    left -= 1
                    right += 1
                    
k = 0

while k < len(switch) : 
    print(switch[k], end = " ") 
    if k % 20 == 19 : 
        print()
        
    k += 1     