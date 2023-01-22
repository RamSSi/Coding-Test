import sys

input = sys.stdin.readline

N, M = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

lt = 0
rt = N
res = 0

while lt <= rt:
    mid = (lt + rt) // 2
    print(mid)
    if a[mid] == M:
        res = mid
        break
    elif a[mid] < M:
        lt = mid + 1
    elif a[mid] > M:
        rt = mid - 1

print(res+1)

# 8 32
# 23 87 65 12 57 32 99 81
# 결과 : 3

# 9 6
# 1 9 2 6 3 7 4 5 8
# 결과 : 6
