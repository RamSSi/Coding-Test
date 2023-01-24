import sys

input = sys.stdin.readline

N, C = map(int, input().split())
hList = [int(input().strip()) for _ in range(N)]
hList.sort()

i = 0
res = 0

lt = hList[0]
rt = hList[N-1]


def Count(mid):
    cnt = 1
    curr = 0
    for i in range(1, N):
        if hList[i] - hList[curr] >= mid:
            curr = i
            cnt += 1
    return cnt


while lt <= rt:
    mid = (lt + rt) // 2
    if Count(mid) >= C:
        res = mid
        lt = mid + 1
    else:
        rt = mid - 1

print(res)
