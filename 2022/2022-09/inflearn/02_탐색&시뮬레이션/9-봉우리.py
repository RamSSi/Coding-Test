import sys

input = sys.stdin.readline

N = int(input())
nlist = [list(map(int, input().split())) for _ in range(N)]

dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
cnt = 0

for i in range(N):
    for j in range(N):
        curr = nlist[i][j]
        print(i, j, curr)
        for (x, y) in dir:
            if 0 <= i + x < N and 0 <= j + y < N:
                print(nlist[i + x][j + y])
                if curr <= nlist[i + x][j + y]:
                    break
        else:
            cnt += 1
print(cnt)