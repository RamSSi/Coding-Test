import sys

input = sys.stdin.readline

a = [list(input().split()) for _ in range(7)]
res = 0

for i in range(7):
    for j in range(3):
        for k in range(2):
            if a[i][j+k] != a[i][j+4-k]:
                break
        else:
            res += 1
        for l in range(2):
            if a[j+l][i] != a[j+4-l][i]:
                break
        else:
            res += 1

print(res)
