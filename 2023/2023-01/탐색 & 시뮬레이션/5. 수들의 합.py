import sys

input = sys.stdin.readline

N, M = map(int, input().split())
nlist = list(map(int, input().split()))

res = 0


# for i in range(N):
#     sum = 0
#     for j in range(i, N):
#         sum += nlist[j]
#         if sum == M:
#             res += 1
#             break

lt = 0
rt = 1
sum = nlist[lt]
while True:
    if sum < M:
        if rt < N:
            sum += nlist[rt]
            rt += 1
        else:
            break
    elif sum == M:
        res += 1
        sum -= nlist[lt]
        lt += 1
    else:
        sum -= nlist[lt]
        lt += 1

print(res)
