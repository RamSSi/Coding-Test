import sys
R, C = map(int, input().split())
alist = [list(map(int, sys.stdin.readline().split())) for _ in range(R)]

blist = [[0] * R for _ in range(C)]



cc = 0
for i in range(C):
    rr = R - 1
    for j in range(R):
        blist[i][j] = alist[rr][i]
        rr -= 1

print(alist, blist)
