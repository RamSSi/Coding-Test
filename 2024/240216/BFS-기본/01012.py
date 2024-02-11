# 01012 유기농 배추

import sys
from collections import deque
dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]
for a in range(int(input())):
    m, n, k = map(int, sys.stdin.readline().split())
    grid = [[0] * m for _ in range(n)]
    v = [[False] * m for _ in range(n)]
    q = deque()
    cnt = 0

    for _ in range(k):
        y, x = map(int, sys.stdin.readline().split())
        grid[x][y] = 1
        
    for i in range(n):
        for j in range(m):
            if v[i][j] == False and grid[i][j] == 1:
                cnt += 1
                q.append((i, j))
                v[i][j] == True
                grid[i][j] = 0
                while q:
                    cx, cy = q.popleft()
                    for d in range(4):
                        x, y = cx + dir[d][0], cy + dir[d][1]
                        if 0 <= x < n and 0 <= y < m:
                            if v[x][y] == False and grid[x][y] == 1:
                                q.append((x, y))
                                v[x][y] = True
    print(cnt)