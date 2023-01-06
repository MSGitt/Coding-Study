word = input()
a = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="] 
result = 0

for i in a :
    word = word.replace(i, "k") 
    
print(len(word))
