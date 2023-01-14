import sys
from collections import deque
R, C = map(int, sys.stdin.readline().split())
field = [sys.stdin.readline().split() for _ in range(R)]
cnt = R * C
camera = []

for i in range(R):
    for j in range(C):
        if field[i][j] != '0':
            camera.append((i, j))
            cnt -= 1

def cctv(num):
    return turn[int(num)-1]


turn = [[],
        [[0], [1], [2], [3]], 
        [[0, 2], [1, 3]],
        [[0, 1], [1, 2], [2, 3], [3, 0]], 
        [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]], 
        [[0, 1, 2, 3]]]

direction = [(1, 0), (0, 1), (-1, 0), (-1, 0)]

# camera : 카메라 좌표 list
# cnt : 빈칸 수

def bfs(r, c, dir, flag):
    rr, cc = dir
    nr, nc = r + rr, c + cc
    while(True):
        if nr < 0 or nc < 0 or nr == R or nc == C:
            break
        if field[nr][nc] == '6':
            flag[nr][nc] = '6'
            break
        elif field[nr][nc] == '0':
            flag[nr][nc] == '#'
            cnt -= 1
        elif field[nr][nc] == '#':
            continue



def view(num):
    while(True):
        for i in cctv(num):
