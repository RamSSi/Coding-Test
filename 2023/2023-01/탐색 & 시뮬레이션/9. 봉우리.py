import sys

input = sys.stdin.readline

N = int(input())
a = [list(map(int, input().split())) for _ in range(N-2)]

a.insert(0, [0] * N)
a.append([0] * N)

for x in a:
    x.insert(0, 0)
    x.append(0)

dir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
res = 0

for i in range(1, N-1):
    for j in range(1, N-1):
        curr = a[i][j]
        for (x, y) in dir:
            if curr < a[i+x][j+y]:
                break
        else:
            res += 1

print(res)

# 7
# 5 3 7 2 3
# 3 7 1 6 1
# 7 2 5 3 4
# 4 3 6 4 1
# 8 7 3 5 2

# 10
