import sys

input = sys.stdin.readline

N, M = map(int, input().split())
pList = list(map(int, input().split()))
pList.sort()

cnt = 0
# lt = 0
# hv = N-1

# while lt < hv:
#     if lt == hv:
#         cnt += 1
#         break
#     if pList[hv] >= M:
#         cnt += 1
#         hv -= 1
#     elif pList[hv] + pList[lt] <= M:
#         cnt += 1
#         lt += 1
#         hv -= 1
#     else:
#         cnt += 1
#         hv -= 1

while pList:
    if len(pList) == 1:
        cnt += 1
        break
    if pList[0] + pList[-1] > M:
        pList.pop()
        cnt += 1
    else:
        pList.pop(0)
        pList.pop()
        cnt += 1

print(cnt)
