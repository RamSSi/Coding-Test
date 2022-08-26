import sys

input = sys.stdin.readline

N, M = map(int, input().split())
slist = list(map(int, input().split()))

l = max(slist)
r = sum(slist)

print(l, r)
def save(m):
    size = m
    cnt = 1
    print(m)
    for i in slist:
        if size - i > 0:
            print(i, "size - i > 0")
            size -= i
        elif size - i == 0:
            print(i, "size - i = 0")
            cnt += 1
            size = m
        elif size - i < 0:
            print(i, "size - i < 0")
            cnt += 1
            size = m - i
    return cnt

while l <= r:
    mid = (l + r) // 2
    if mid == l:
        print(l)
        break
    result = save(mid)
    print(result)
    if result == M:
        print(mid)
        break
    elif result > M:
        print("l = mid + 1")
        l = mid + 1
    else:
        print("r = mid - 1")
        r = mid - 1
