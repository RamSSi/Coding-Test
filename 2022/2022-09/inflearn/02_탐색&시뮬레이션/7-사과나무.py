import sys

input = sys.stdin.readline

N = int(input())
trees = [list(map(int, input().split())) for _ in range(N)]

apple = 0

# for i in range(N):
#     if i <= N // 2:
#         a = N // 2 - i
#         for _ in range(2 * i + 1):
#             apple += trees[i][a]
#             a += 1
#     else:
#         a = i - N // 2
#         for _ in range(2 * (N - i) - 1):
#             apple += trees[i][a]
#             a += 1
# print(apple)

s = e = N // 2
for i in range(N):
    for j in range(s, e + 1):
        apple += trees[i][j]
    if i < N // 2:
        s -= 1
        e += 1
    else:
        s += 1
        e -= 1

print(apple)