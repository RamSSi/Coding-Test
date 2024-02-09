# 02178 미로탐색

import sys
from collections import deque

dir = [(-1, 0), (0, -1), (1, 0), (0, 1)]

n, m = map(int, input().split())
v = [[0] * m for _ in range(n)]
b = []
dist = 1
q = deque()
for _ in range(n):
    b.append(list(map(int, sys.stdin.readline().strip())))
for i in range(n):
    for j in range(m):
        if b[i][j] == 1 and v[i][j] == 0:
            v[i][j] = 1
            b[i][j] = dist
            q.append((i, j))
        while q:
            cx, cy = q.popleft()
            for d in range(4):
                dx, dy = cx + dir[d][0], cy + dir[d][1]
                if dx < 0 or dy < 0 or dx >= n or dy >= m: continue
                if b[dx][dy] == 1 and v[dx][dy] == 0:
                    v[dx][dy] = 1
                    b[dx][dy] = dist
                    if dx == n-1 and dy == m-1:
                        print(b[dx][dy])
                        q = []
                        break
                    q.append((dx, dy))
                
            dist += 1
print(*b, sep="\n")