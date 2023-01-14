import sys

input = sys.stdin.readline

N, M = map(int, input().split())
nlist = list(map(int, input().split()))
nlist.sort()

l = 0
r = N - 1
while l <= r:
    mid = (l + r) // 2
    if nlist[mid] == M:
        print(mid + 1)
        break
    elif nlist[mid] > M:
        r = mid - 1
    else:
        l = mid + 1

# curr = N // 2
# while True:
#     if nlist[curr] == M:
#         print(curr + 1)
#         break
#     elif nlist[curr] < M:
#         curr = (curr + N) // 2
#     else:
#         curr = curr // 2