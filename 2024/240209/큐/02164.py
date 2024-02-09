# 02164 카드2

import sys
from collections import deque

q = deque(range(1, int(input())+1))
f = 0
while len(q) > 1:
    q.popleft()
    q.append(q.popleft())
print(q[0])