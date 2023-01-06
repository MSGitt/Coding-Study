import sys
from itertools import combinations


n, m = map(int, sys.stdin.readline().split())

number = [i for i in range(1, n+1)]

k = list(combinations(number, m))

for i in k :
    print(*i)