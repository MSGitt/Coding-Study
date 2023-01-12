def solution(m, n, puddles):
    answer = 0
    
    dp = [[0] * m for i in range(n)]
    
    for i in puddles :
        dp[i[1]-1][i[0]-1] = -1   
    
    for i in range(m) :
        if dp[0][i] == -1 :
            break
        dp[0][i] = 1
        
    for i in range(n) :
        if dp[i][0] == -1 :
            break
        dp[i][0] = 1
        
    for i in range(1, n) :
        for j in range(1, m) :
            if dp[i][j] == -1 :
                continue 
                
            if dp[i-1][j] == -1 or dp[i][j-1] == -1 :
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                
            else :
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
    
    return dp[-1][-1] % 1000000007