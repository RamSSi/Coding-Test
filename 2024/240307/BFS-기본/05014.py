# 05014 스타트링크

import sys
from collections import deque

input = sys.stdin.readline
v = set()

f, s, g, u, d = map(int, input().split())
q = deque([(s, 0)])
cnt = 0

while q:
    curr, cnt = q.popleft()
    if curr == g:
        print(cnt)
        break
    cnt += 1
    up = curr + u
    down = curr - d
    if up not in v and 1 <= up <= f:
        q.append((up, cnt))
        v.add(up)
    if down not in v and 1 <= down <= f:
        q.append((down, cnt))
        v.add(down)
    if not(q): print("use the stairs")

# ==========================================
# 다른 방법으로 풀어보기..