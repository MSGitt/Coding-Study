n = int(input()) 

words = [] 

for i in range(n) : 
    word = str(input())
    length = len(word) 
    words.append((length, word)) 
    
words = list(set(words)) 

words.sort(key = lambda x : (x[0], x[1]))

for k in words : 
    print(k[1])
        