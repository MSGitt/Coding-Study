import math

def solution(n, k):
    
    number = [i for i in range(1, n+1)]
    result = []
    k -= 1
    
    while number :
        
        temp = k // math.factorial(n-1)
        result.append(number[temp])
        
        del number[temp]
        
        k %= math.factorial(n-1)
        n -= 1
        
    return result