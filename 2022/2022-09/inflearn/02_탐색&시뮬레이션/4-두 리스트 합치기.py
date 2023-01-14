import sys
N = int(input())
nlist = list(map(int, sys.stdin.readline().split()))
M = int(input())
mlist = list(map(int, sys.stdin.readline().split()))

i, j = 0, 0
while i < N or j < M:
    if nlist[i] < mlist[j]:
        print(nlist[i], end= ' ')
        i += 1
    elif nlist[i] > mlist[j]:
        print(mlist[j], end = ' ')
        j += 1
    else:
        print(nlist[i], mlist[j], end = ' ')
        i, j = i + 1, j + 1
    if i == N:
        while j < M:
            print(mlist[j], end = ' ')
            j += 1
    elif j == M:
        while i < N:
            print(nlist[i], end = ' ')
            i += 1