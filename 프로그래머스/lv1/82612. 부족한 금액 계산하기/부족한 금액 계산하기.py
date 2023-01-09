def solution(price, money, count):
    
    total = price * (count) * (count + 1) // 2
    
    if money >= total :
        return 0

    return total - money