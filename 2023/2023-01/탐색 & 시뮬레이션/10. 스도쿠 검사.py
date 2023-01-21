import sys

input = sys.stdin.readline

a = [list(map(int, input().split())) for _ in range(9)]


def check(a):
    for i in range(9):
        k = [0] * 9
        for j in (a[i]):
            if k[j-1] == 1:
                return False
            else:
                k[j-1] += 1

        k = [0] * 9
        for j in range(9):
            if k[a[i][j]-1] == 1:
                return False
            else:
                k[a[i][j]-1] += 1

        k = [0] * 9
        for x in range(3):
            for y in range(3):
                if k[a[x][y]-1] == 1:
                    return False
    return True


if check(a) == True:
    print("YES")
else:
    print("NO")

# 1 4 3 6 2 8 5 7 9
# 5 7 2 1 3 9 4 6 8
# 9 8 6 7 5 4 2 3 1
# 3 9 1 5 4 2 7 8 6
# 4 6 8 9 1 7 3 5 2
# 7 2 5 8 6 3 9 1 4
# 2 3 7 4 8 1 6 9 5
# 6 1 9 2 7 5 8 4 3
# 8 5 4 3 9 6 1 2 7
