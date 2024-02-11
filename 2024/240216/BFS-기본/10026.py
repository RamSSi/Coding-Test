# 10026 적록색약

import sys
from collections import deque

dir = [(-1, 0), (0, -1), (1, 0), (0, 1)]
n = int(input())
grid = list(list(sys.stdin.readline().rstrip()) for _ in range(n))
v = [[False] * n for _ in range(n)]
v_2 = [[False] * n for _ in range(n)]
rc, gc, bc, rgc = 0, 0, 0, 0

def bfs(i, j, c, v):
    q = deque()
    cnt = 0
    if not v[i][j] and grid[i][j] in c:
        cnt += 1
        q.append((i, j))
        v[i][j] = True
        while q:
            rx, ry = q.popleft()
            for d in range(4):
                x, y = rx + dir[d][0], ry + dir[d][1]
                if 0 <= x < n and 0 <= y < n:
                    if not v[x][y] and grid[x][y] in c:
                        q.append((x, y))
                        v[x][y] = True
    return cnt

for i in range(n):
    for j in range(n):
        rc += bfs(i, j, ['R'], v)
        gc += bfs(i, j, ['G'], v)
        bc += bfs(i, j, ['B'], v)
        rgc += bfs(i, j, ['R', 'G'], v_2)

print(rc + gc + bc, rgc + bc)