import sys

input = sys.stdin.readline

N, M = map(int, input().split())
musics = list(map(int, input().split()))

res = 0


def song(mid):
    save = 0
    dvd = 1
    for x in musics:
        if save + x > mid:
            dvd += 1
            save = x
        elif save + x <= mid:
            save += x
    return dvd


if (N == M):
    res = max(musics)
else:
    lt = 1
    rt = sum(musics)
    while lt <= rt:
        mid = (lt + rt) // 2
        if song(mid) > M:
            lt = mid + 1
        else:
            res = mid
            rt = mid - 1
print(res)
