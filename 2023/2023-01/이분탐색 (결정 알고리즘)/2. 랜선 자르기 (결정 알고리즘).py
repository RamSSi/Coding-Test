import sys

input = sys.stdin.readline

K, N = map(int, input().split())
lans = []
maxL = 0
for i in range(K):
    lans.append(int(input()))
    if lans[i] > maxL:
        maxL = lans[i]

lt = 1
rt = maxL

res = 0

while lt <= rt:
    cnt = 0
    mid = (lt + rt) // 2
    for i in range(K):
        cnt += (lans[i] // mid)
    if cnt < N:
        rt = mid - 1
    elif cnt >= N:
        res = mid
        lt = mid + 1

print(res)
