# 15486 : 퇴사 2
import sys, itertools

input = sys.stdin.readline
comb = []
N = int(input())

counseling = []
confirm = [0] * N

for _ in range(N):
    day, pay = map(sys.stdin.readline().split())
    counseling.append((_, day, pay))

for i in range(N, 0, -1):
    comb += list(itertools.combinations(list(range(N)), i))

