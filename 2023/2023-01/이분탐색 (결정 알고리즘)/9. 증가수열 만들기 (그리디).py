import sys

input = sys.stdin.readline

N = int(input())
n = list(map(int, input().split()))

resL = []
res = ""
lt = 0
rt = N-1
last = 0

while lt <= rt:
    if last < n[lt]:
        resL.append((n[lt], "L"))
        lt += 1
    if last < n[rt]:
        resL.append((n[rt], "R"))
        rt -= 1
    resL.sort()
    if len(resL) == 0:
        break
    for (num, dir) in resL:
        res += dir
    else:
        last = num

    resL.clear()

print(len(res))
print(res)
