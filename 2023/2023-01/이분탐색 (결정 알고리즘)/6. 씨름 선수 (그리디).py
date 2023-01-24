import sys

input = sys.stdin.readline

N = int(input())
pList = []
for i in range(N):
    a, b = map(int, input().split())
    pList.append((a, b))

# =========================
# 이중 for문
# pList.sort()

# cnt = 0
# for (a, b) in pList:
#     for (x, y) in pList:
#         if a < x and b < y:
#             break
#     else:
#         cnt += 1
# =========================

pList.sort(reverse=True)

cnt = 0
largest = 0
for (a, b) in pList:
    if b > largest:
        cnt += 1
        largest = b

print(cnt)
