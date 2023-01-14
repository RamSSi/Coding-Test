# 2493 : 탑

# import sys

# nlist = []
# result = [0]

# N = int(input())
# maxidx = 0

# nlist = list(map(int, sys.stdin.readline().split()))

# for i in range(1, N):
#     if nlist[maxidx] < nlist[i]:    # 제일 높은 탑보다 낮으면 0
#         result.append(0)
#         continue

#     idx = i - 1 # 비교 시작
#     while nlist[idx] < nlist[i] and idx >= maxidx:    # 왼쪽 탑보다 작으면 반복
#         idx -= 1
#     result.append(idx + 1)
#     if nlist[idx] >= nlist[maxidx]:
#         maxidx = idx

# print(*result, sep=' ')


# import sys

# n = int(input())
# nlist = list(map(int, sys.stdin.readline().split()))
# answer = [0 for _ in range(n)]
# stack = [] # 이전 숫자 스택

# for i in range(n):
#     while stack:
#         if nlist[i] <= stack[-1][1]:
#             answer[i] = stack[-1][0] + 1
#             break
#         else:
#             stack.pop()
#     stack.append([i, nlist[i]])

# print(*answer)

import sys

n = int(input())
nlist = list(map(int, sys.stdin.readline()) for _ in range(n))

answer = [0 for _ in range(n)]
stack = []

for i in range(n):
    while stack:
        if nlist[i] > stack[-1][1]:
            answer[i] = stack[-1][0] + 1
            break
        else:
            stack.pop()