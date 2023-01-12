def solution(N, number):
    
    if N == number :
        return 1
    
    dp = [set() for i in range(9)] 
    
    for i in range(1, 9): 
        dp[i].add(int(str(N)*i)) 
        for j in range(i//2 + 1):
            for r1 in dp[j]:
                for r2 in dp[i-j]:
                    dp[i].add(r1 + r2)
                    dp[i].add(r1 - r2)
                    dp[i].add(r2 - r1)
                    dp[i].add(r1 * r2)
                    if r2 != 0 :
                        dp[i].add(r1 // r2)
                    if r1 != 0 :
                        dp[i].add(r2 // r1)
                    
        if number in dp[i]:
            return i
        
    return -1