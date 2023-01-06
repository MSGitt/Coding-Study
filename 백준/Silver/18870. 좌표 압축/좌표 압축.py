import sys
import copy


n = int(sys.stdin.readline())

number = list(map(int, sys.stdin.readline().split()))
dic = {}
rank = 0

n1 = sorted(set(number))

for i in n1 :
    dic[i] = rank
    rank += 1 
    
for i in number :
    print(dic[i])