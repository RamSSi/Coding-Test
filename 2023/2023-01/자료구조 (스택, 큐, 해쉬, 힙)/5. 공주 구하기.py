import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())

# 내 풀이
# queue = [i for i in range(1, N+1)]
# cnt = 0
# while len(queue) != 1:
#     x = queue.pop(0)
#     cnt += 1
#     if cnt == K:
#         cnt = 0
#         continue
#     queue.append(x)

# print(queue.pop())

dq = deque(list(range(1, N+1)))
while dq:
    for _ in range(K-1):
        cur = dq.popleft()
        dq.append(cur)
    dq.popleft()
    if len(dq) == 1:
        print(dq[0])
        dq.popleft()
