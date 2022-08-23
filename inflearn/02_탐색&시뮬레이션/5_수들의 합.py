import sys

N, M = map(int, input().split())
nlist = list(map(int, input().split()))

cnt = 0
for i in range(N):
    a = 0
    for j in range(i, N):
        if a < M:
            a += nlist[j]
        elif a > M:
            a = 0
            break
        if a == M:
            cnt += 1
            a = 0
            break
            
print(cnt)