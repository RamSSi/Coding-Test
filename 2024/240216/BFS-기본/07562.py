# 07562 나이트의 이동

import sys
from collections import deque

dir = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]

def bfs(q, v, a, b):
    while q:
        x, y, cnt = q.popleft()
        if x == a and y == b:
            return cnt
        for d in range(8):
            dx, dy = x + dir[d][0], y + dir[d][1]
            if 0 <= dx < l and 0 <= dy < l:
                if v[dx][dy] == False:
                    q.append((dx, dy, cnt + 1))
                    v[dx][dy] = True

for _ in range(int(input())):
    l = int(input())
    x, y = map(int, sys.stdin.readline().split())
    a, b = map(int, sys.stdin.readline().split())
    print(bfs(deque([(x, y, 0)]), [[False] * l for _ in range(l)], a, b))

# 현재 장소에서 가장 가까운 경로로 이동하도록 변경해보자