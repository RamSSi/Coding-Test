import sys

input = sys.stdin.readline

# def turn0(a, c):
#     newli = []
#     for _ in range(N):
#         newli.append(nlist[a-1][c])
#         c = (c + 1) % N
#     nlist[a-1] = newli

# def turn1(a, c):
#     newli = []
#     c = N - c
#     for _ in range(N):
#         newli.append(nlist[a-1][c])
#         c = (c + 1) % N
#     nlist[a-1] = newli

N = int(input())
nlist = [list(map(int, input().split())) for _ in range(N)]

for i in range(int(input())):
    a, b, c = map(int, input().split())
    if b == 0:
        # turn0(a, c)
        for i in range(c):
            nlist[a-1].append(nlist[a-1].pop(0))
    elif b == 1:
        # turn1(a, c)
        for i in range(c):
            nlist[a-1].insert(0, nlist[a-1].pop())

print(nlist)

a = 0
b = N - 1

result = 0

for i in range(N):
    for j in range(a, b+1):
        result += nlist[i][j]
    
    if i < N // 2:
        a += 1
        b -= 1
    else:
        a -= 1
        b += 1

print(result)