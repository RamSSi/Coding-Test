# 07576 토마토

import sys
from collections import deque
input = sys.stdin.readline
def bfs(day, queue):
    tq = deque()
    while queue:
        (cx, cy) = queue.popleft()
        for d in range(4):
            dx, dy = cx + dir[d][0], cy + dir[d][1]
            if dx < 0 or dy < 0 or dx >= n or dy >= m or t[dx][dy] == -1: continue
            if t[dx][dy] == 0 and v[dx][dy] == 0:
                t[dx][dy] = day
                v[dx][dy] = 1
                tq.append((dx,dy))
    return tq
            
dir = [(-1, 0), (0, -1), (1, 0), (0, 1)]
m, n = map(int, input().split())
q = deque()
t = []
v = [[0] * m for _ in range(n)]
day = 0
ans = 0

for _ in range(n):
    t.append(list(map(int, input().split())))
    
for i in range(n):
    for j in range(m):
        if v[i][j] == 0 and t[i][j] == 1:
            q.append((i, j))
            v[i][j] = 1
while q:
    result = day
    day += 1
    q = bfs(day, q)
for i in range(n):
    for j in range(m):
        if t[i][j] == 0: result = -1

print(result)