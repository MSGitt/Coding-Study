import sys

word = list(sys.stdin.readline().rstrip())

i, start = 0, 0

while i < len(word) :
    
    if word[i] == '<' :
        i += 1
        while word[i] != '>' :
            i += 1
            
        i += 1
        
    elif word[i].isalnum() :
        start = i
        
        while i < len(word) and word[i].isalnum() :
            i += 1
            
        word[start: i] = word[start: i][::-1]
        
    else :
        i += 1
        
print(''.join(word))