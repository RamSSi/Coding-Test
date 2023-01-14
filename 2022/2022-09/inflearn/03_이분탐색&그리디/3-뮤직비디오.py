import sys
input = sys.stdin.readline

N, M = map(int, input().split())
music = list(map(int, input().split()))

def save(size):
    result = [[]]
    s = size
    cnt = 0
    for m in music:
        if s - m < 0:
            cnt += 1
            result.append([m])
            s = size - m
        elif s - m == 0:
            result[cnt].append(m)
            s = size
        else:
            result[cnt].append(m)
            s -= m
    return cnt + 1

lt = max(music)
rt = sum(music)
size = 0
if M == 1:
    size = rt
elif N == M:
    size = lt
else:
    while lt <= rt:
        mid = (lt + rt) // 2
        cnt = save(mid)
        if M >= cnt:
            size = mid
            rt = mid - 1
        elif M < cnt:
            lt = mid + 1
print(size)