import sys

n = int(sys.stdin.readline())

def mul(a, b):
    cal = []
    for i in range(2):
        temp = []
        for j in range(2):
            num = 0
            for k in range(2):
                num += a[i][k] * b[k][j]
            temp.append(num % 1000000007)
        cal.append(temp)
        
    return cal

def fib(mat, n) : 
    
    if n == 1 :
        return mat
                                
    temp = fib(mat, n // 2)
    
    result = mul(temp, temp)
    
    if n % 2 == 0 :
        return result
    
    else : 
        return mul(result, k)
    
k = [[1, 1], [1, 0]]
result = fib(k, n)

print(result[0][1])     