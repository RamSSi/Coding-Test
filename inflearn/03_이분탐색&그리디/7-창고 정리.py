import sys

input = sys.stdin.readline

L = int(input())
nlist = list(map(int, input().split()))
M = int(input())

nlist.sort()

for i in range(M):
    nlist[L-1] -= 1
    nlist[0] += 1
    nlist.sort()

print(nlist[L-1] - nlist[0])