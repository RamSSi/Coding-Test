import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

# queue = deque([])
# q = list(map(int, input().split()))
# for i in range(N):
#     queue.append((i, q[i]))

# cnt = 0

# while queue:
#     (curr, r) = queue.popleft()
#     cnt += 1
#     for (a, b) in queue:
#         print(r, b)
#         if r < b:
#             queue.append((curr, r))
#             cnt -= 1
#             break
#     else:
#         if curr == M:
#             print(cnt)
#             break

queue = [(idx, val) for idx, val in enumerate(list(map(int, input().split())))]

cnt = 0
while True:
    curr = queue.popleft()
    if any(curr[1] < x[1] for x in queue):
        queue.append(curr)
    else:
        cnt += 1
        if curr[0] == M:
            print(cnt)
            break
