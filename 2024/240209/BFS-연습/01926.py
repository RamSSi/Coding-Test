# 01926 그림

import sys
from collections import deque

q = deque()
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

num = 0
area = 0
mx = 0

n, m = map(int, sys.stdin.readline().split())
a = []
v = [[0]*m for _ in range(n)]
for _ in range(n):
    a.append(list(map(int, sys.stdin.readline().split())))

for i in range(n):
    for j in range(m):
        if a[i][j] == 1 and v[i][j] == 0:
            num += 1
            area += 1
            q.append((i, j))
            v[i][j] = 1
            while q:
                cx, cy = q.popleft()
                for dir in range(4):
                    x, y = cx + dx[dir], cy + dy[dir]
                    if (x < 0 or y < 0 or x >= n or y >= m): continue
                    if a[x][y] == 1 and v[x][y] == 0:
                        v[x][y] = 1
                        area += 1
                        q.append((x, y))
        mx = max(mx, area)
        area = 0

print(num, mx)

# 파이썬 2차원 배열 생성 시 유의할 것!
# 2차원 배열 초기화
# a = [[0] * m for _ in range(n)]