# 02178 불!

import sys
from collections import deque

jh = deque()
fire = deque()
n, m = map(int, input().split())
jh_v = [[0] * m for _ in range(n)]
fire_v = [[0] * m for _ in range(n)]
second = 0
dir = [(-1, 0), (0, -1), (1, 0), (0, 1)]
maps = []

for i in range(n):
    maps.append(list(sys.stdin.readline().strip()))

for i in range(n):
    for j in range(m):
        if maps[i][j] == 'J':
            jh.append((i, j, 0))
            jh_v[i][j] = 1
        elif maps[i][j] == 'F':
            fire.append((i, j))
            fire_v[i][j] = 1

def fire_bfs(q):
    fq = deque()
    while q:
        (cx, cy) = q.popleft()
        for i in range(4):
            dx, dy = cx + dir[i][0], cy + dir[i][1]
            if dx < 0 or dy < 0 or dx >= n or dy >= m:
                continue
            if maps[dx][dy] == '#':
                fire_v[dx][dy] = 1
            if maps[dx][dy] == '.' or maps[dx][dy] == 'J':
                maps[dx][dy] = 'F'
                fire_v[dx][dy] = 1
                fq.append((dx, dy))
            # elif maps[dx][dy] == '0' or maps[dx][dy] == '#':
            #     continue
    return fq
    
def jh_bfs(q):
    s = 0
    jq = deque()
    while q:
        (cx, cy, s) = q.popleft()
        cnt = 0
        for i in range(4):
            dx, dy = cx + dir[i][0], cy + dir[i][1]
            if dx < 0 or dy < 0 or dx >= n or dy >= m:
                return deque(), (dx, dy, s+1)
            if maps[dx][dy] == '.' and jh_v[dx][dy] == 0 and fire_v[dx][dy] == 0:
                jh_v[dx][dy] = 1
                maps[dx][dy] = 'J'
                jq.append((dx, dy, s+1))
    return jq, (-1, -1 ,s + 1)
    
x = -1
y = -1
while jh:
    fire = fire_bfs(fire)
    jh, (x, y, second) = jh_bfs(jh)
    if x != -1 or y != -1:
        break
    else:
        second = "IMPOSSIBLE"
print(second)

# ============================================

import sys
from collections import deque

n, m = map(int, input().split())
dir = [(-1, 0), (0, -1), (1, 0), (0, 1)]

maze = list(list(sys.stdin.readline().rstrip()) for _ in range(n))
jh_v = [[0] * m for _ in range(n)]

fire = deque()
jh = deque()

for i in range(n):
    for j in range(m):
        if maze[i][j] == 'J':
            jh.append((i, j))
        elif maze[i][j] == 'F':
            fire.append((i, j))
    
def solve(jh, fire):
    cnt = 0
    while jh:
        # fire
        next_fire = deque()
        while fire:
            (fx, fy) = fire.popleft()
            for d in range(4):
                x, y = fx + dir[d][0], fy + dir[d][1]
                if 0 <= x < n and 0 <= y < m:
                    if maze[x][y] == 'J' or maze[x][y] == '.':
                        maze[x][y] = 'F'
                        next_fire.append((x, y))
        fire = next_fire
        
        cnt += 1
        # jihoon
        next_jh = deque()
        while jh:
            (jx, jy) = jh.popleft()
            for d in range(4):
                x, y = jx + dir[d][0], jy + dir[d][1]
                if 0 <= x < n and 0 <= y < m:
                    if maze[x][y] == '.':
                        next_jh.append((x, y))
                        maze[x][y] = "J"
                else:
                    return cnt
        jh = next_jh
    return "IMPOSSIBLE"

print(solve(jh, fire))