# 02468 안전 영역
import sys
from collections import deque
input = sys.stdin.readline

dir = [(-1, 0), (0, -1), (1, 0), (0, 1)]

n = int(input())
maps = [list(map(int, input().split())) for _ in range(n)]

minH = 100
maxH = 0

result = 0
before = 0

for i in range(n):
    maxH = max(max(maps[i]), maxH)

for num in range(0, maxH):
    v = [[False] * n for _ in range(n)]
    q = deque()
    cnt = 0
    for i in range(n):
        for j in range(n):
            if maps[i][j] > num and v[i][j] == False:
                v[i][j] = True
                cnt += 1
                q.append((i, j))
                while q:
                    x, y = q.popleft()
                    for d in range(4):
                        dx, dy = x + dir[d][0], y + dir[d][1]
                        if 0 <= dx < n and 0 <= dy < n:
                            if maps[dx][dy] > num and v[dx][dy] == False:
                                v[dx][dy] = True
                                q.append((dx, dy))
    if cnt > result:
        result = cnt
print(result)