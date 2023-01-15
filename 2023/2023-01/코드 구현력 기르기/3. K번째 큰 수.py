import sys
from itertools import combinations

input = sys.stdin.readline

N, K = map(int, input().split())
sumList = set()
for (a, b, c) in combinations(list(map(int, input().split())), 3):
    sumList.add(a+b+c)
sumList = list(sumList)
sumList.sort(reverse=True)

print(sumList[K-1])
