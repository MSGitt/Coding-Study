import sys 


a, b = map(int, sys.stdin.readline().split()) 
num = list(map(int, sys.stdin.readline().split()))

que = [i for i in range(1, a+1)] 
result = 0

for i in range(b) : 
    if que.index(num[i]) < len(que) - que.index(num[i]) :
        while True : 
            if que[0] == num[i] : 
                del que[0]
                break 
                
            else :
                que.append(que[0])
                del que[0]
                result += 1 
    
    else : 
        while True : 
            if que[0] == num[i] : 
                del que[0]
                break 
                
            else : 
                que.insert(0, que[-1])
                del que[-1]
                result += 1 
                
print(result)
