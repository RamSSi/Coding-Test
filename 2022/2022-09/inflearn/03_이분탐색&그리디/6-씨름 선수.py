import sys

input = sys.stdin.readline

n = int(input())

players = []
for _ in range(n):
    h, w = map(int, input().split())
    players.append((h, w))

players.sort(reverse= True)

print(players)

height = 0
cnt = 0
for i in range(n):
    if i == 0:
        cnt += 1
        continue
    for j in range(0, i):
        prevH, prevW = players[j]
        h, w = players[i]
        if prevW >= w:
            break
        if j == i-1:
            cnt += 1

print(cnt)