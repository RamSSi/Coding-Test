import sys

input = sys.stdin.readline

N, C = map(int, input().split())

xlist = list(int(input()) for _ in range(N))

xlist.sort()

def count(dist):
    cnt = 1
    prev = xlist[0]
    for i in range(1, N):
        if xlist[i] - prev >= dist:
            cnt += 1
            prev = xlist[i]
    return cnt

lt = xlist[0]
rt = xlist[N-1]

result = 0
while lt <= rt:
    mid = (lt + rt) // 2
    if count(mid) >= C:
        result = mid
        lt = mid + 1
    else:
        rt = mid - 1

print(result)