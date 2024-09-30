# 02667 단지번호 붙이기

import sys
from collections import deque

q = deque()
input = sys.stdin.readline
dir = [(-1, 0), (0, -1), (1, 0), (0, 1)]

n = int(input())
maps = []
for _ in range(n):
    maps.append(list(input().rstrip()))

result = []
num = 0

for i in range(n):
    for j in range(n):
        cnt = 0
        if maps[i][j] == '1':
            num += 1
            q.append((i,j))
            maps[i][j] = num
            while q:
                x, y = q.popleft()
                cnt += 1
                for d in range(4):
                    dx, dy = x + dir[d][0], y + dir[d][1]
                    if 0 <= dx < n and 0 <= dy < n and maps[dx][dy] == '1':               
                        q.append((dx, dy))
                        maps[dx][dy] = num
            result.append(cnt)

result.sort()
print(len(result))
print(*result, sep="\n")