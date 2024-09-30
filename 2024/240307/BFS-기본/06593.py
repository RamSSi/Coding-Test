# 06593 상범 빌딩

import sys
from collections import deque
input = sys.stdin.readline

dir = [(-1, 0, 0), (0, -1, 0), (0, 0, -1), 
       (1, 0, 0), (0, 1, 0), (0, 0, 1)]

while True:
    l, r, c = map(int, input().split())
    if l == 0 and r == 0 and c == 0:
        break
    building = []
    exit = 0
    cnt = 0
    message = "Trapped!"

    for _ in range(l):
        b = []
        for _ in range(r):
            b.append(list(input().rstrip()))
        input()
        building.append(b)
        
    q = deque()

    # 출발지와 탈출구 확인
    for i in range(l):
        for j in range(r):
            for k in range(c):
                if building[i][j][k] == 'S':
                    q.append((i, j, k))
                elif building[i][j][k] == 'E':
                    exit = (i, j, k)

    # 탈출
    while q:
        r_q = deque()
        cnt += 1
        for f, x, y in q:
            for d in range(6):
                df, dx, dy = f + dir[d][0], x + dir[d][1], y + dir[d][2]
                if (df, dx, dy) == exit:
                    message = "Escaped in " + str(cnt) + " minute(s)."
                if 0 <= df < l and 0 <= dx < r and 0 <= dy < c:
                    if building[df][dx][dy] == '.':
                        building[df][dx][dy] = 'S'
                        r_q.append((df, dx, dy))
        q = r_q
    print(message)