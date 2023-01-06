import sys

n = int(sys.stdin.readline())

dp1 = [0] * 3
dp2 = [0] * 3

temp1 = [0] * 3
temp2 = [0] * 3

for i in range(n) :   
    a, b, c = map(int, sys.stdin.readline().split())
    for j in range(3) : 
        if j == 0 :
            temp1[j] = a + max(dp1[j], dp1[j + 1])
            temp2[j] = a + min(dp2[j], dp2[j + 1])
            
        elif j == 1 : 
            temp1[j] = b + max(dp1[j - 1], dp1[j], dp1[j + 1])
            temp2[j] = b + min(dp2[j - 1], dp2[j], dp2[j + 1])
            
        else :
            temp1[j] = c + max(dp1[j - 1], dp1[j])
            temp2[j] = c + min(dp2[j - 1], dp2[j])

    for k in range(3) :
        dp1[k] = temp1[k]
        dp2[k] = temp2[k]

print(max(dp1), min(dp2))