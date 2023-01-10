def solution(n, money):
    
    money.sort()
    
    answer = 0
    
    dp = [0] * (n + 1)
    dp[0] = 1
    
    for i in money :
        for j in range(i, n + 1) :
            if j >= i :
                dp[j] += dp[j - i]
                
    return dp[n] % 1000000007
    