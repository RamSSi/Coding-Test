import sys

N = int(input())
nlist = [list(map(int, sys.stdin.readline().split())) for i in range(N)]

a, b, c, d = 0, 0, 0, 0
for i in range(N):    
    c += nlist[i][i]
    d += nlist[i][N-1-i]
    for j in range(N):
        a += nlist[i][j]
        b += nlist[j][i]
    maxSum = max(a, b)
    a, b = 0, 0    
maxSum = max(maxSum, c, d)