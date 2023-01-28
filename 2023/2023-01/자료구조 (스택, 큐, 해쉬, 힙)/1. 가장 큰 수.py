import sys

input = sys.stdin.readline

N, M = input().split()
N = list(map(int, N))
M = int(M)
res = []


for i in N:
    while res and i > res[-1]:
        if M == 0:
            break
        res.pop()
        M -= 1
    res.append(i)
if M > 0:
    res = res[:-M]

# for x in res:
#     print(x)

print("".join(map(str, res)))
