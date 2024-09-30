# 02583 영역 구하기

import sys
from collections import deque

q = deque()
input = sys.stdin.readline
dir = [(-1, 0), (0, -1), (1, 0), (0, 1)]

m, n, k = map(int, input().split())
squares = list([0] * m for _ in range(n))
v = list([False] * m for _ in range(n))
result = []
cnt = 0

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            squares[i][j] = 1

for i in range(n):
    for j in range(m):
        if squares[i][j] == 0 and v[i][j] == False:
            cnt += 1
            q.append((i,j))
            v[i][j] = True
            while q:
                x, y = q.popleft()
                for d in range(4):
                    dx, dy = x + dir[d][0], y + dir[d][1]
                    if 0 <= dx < n and 0 <= dy < m and squares[dx][dy] == 0 and v[dx][dy] == False:
                        cnt += 1
                        q.append((dx, dy))
                        v[dx][dy] = True
            result.append(cnt)
            cnt = 0

result.sort()
print(len(result))
print(*result, sep=" ")