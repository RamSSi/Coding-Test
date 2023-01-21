import sys

input = sys.stdin.readline

N = int(input())
li = []

for _ in range(N):
    li.append(list(map(int, input().split())))

M = int(input())

start = 0
end = N
res = 0

for _ in range(M):
    a, b, c = map(int, input().split())
    if b == 0:
        for _ in range(c):
            li[a-1].append(li[a-1].pop(0))
    else:
        for _ in range(c):
            li[a-1].insert(0, li[a-1].pop())

for i in range(N):
    print(start, end-1)
    for j in range(start, end):
        res += li[i][j]
    if i < N//2:
        start += 1
        end -= 1
    else:
        start -= 1
        end += 1
print(res)

# 7
# 5 3 7 2 3
# 3 7 1 6 1
# 7 2 5 3 4
# 4 3 6 4 1
# 8 7 3 5 2
# 3
# 2 0 3
# 5 1 2
# 3 1 4

# 362
