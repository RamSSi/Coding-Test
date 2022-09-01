import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
weight = list(map(int, input().split()))

weight.sort()
small, large = 0, N-1

weight = deque(weight)
cnt = 0
while weight:
    if len(weight) == 1:
        cnt += 1
        break
    if weight[0] + weight[-1] <= M:
        weight.pop()
        # weight.pop(0)
        weight.popleft()
        cnt += 1
    else:
        weight.pop()
        cnt += 1
print(cnt)

# cnt = 0
# while small <= large:
#     if M - large >= small:
#         large -= 1
#         small += 1
#         cnt += 1
#     else:
#         large -= 1
#         cnt += 1
# print(cnt)
