# 07569 토마토

import sys

def bfs(q, day, cnt):
    i = 0
    l = len(q)
    tq = []
    dir = [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]
    while i < l:
        w, x, y = q[i]
        day = max(day, t[w][x][y]-1)
        for d in range(6):
            dw, dx, dy = w + dir[d][0], x + dir[d][1], y + dir[d][2]
            if dw < 0 or dx < 0 or dy < 0 or dw >= h or dx >= n or dy >= m:
                continue
            if t[dw][dx][dy] == 0:
                t[dw][dx][dy] = t[w][x][y] + 1
                tq.append((dw, dx, dy))
                cnt += 1
        i += 1
    return tq, day, cnt

m, n, h = map(int, input().split())
t = []
cnt = 0
day = 0
q = []
for i in range(h):
    t.append([])
    for _ in range(n):
         t[i].append(list(map(int, sys.stdin.readline().split()))) 

for i in range(h):
    for j in range(n):
        for k in range(m):
            if t[i][j][k] == 0: continue
            if t[i][j][k] == 1:
                q.append((i, j, k))
            cnt += 1

while q:
    q, day, cnt = bfs(q, day, cnt)

if cnt == m*n*h: print(day)
else: print(-1)