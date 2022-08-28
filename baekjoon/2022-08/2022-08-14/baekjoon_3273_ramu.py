# 3273 : 두 수의 합

import sys
N = int(input())
nlist = list(map(int, sys.stdin.readline().split()))
X = int(input())

b = {}
for n in nlist:
    b[n] = False

a = []
cnt = 0
for n in nlist:
    if X - n == n:
        a.append(n)
        continue
    try:
        c = b[X-n]
    except KeyError:
        continue
    if c is False:
        b[X-n] = True
        b[n] = True
        cnt += 1
print(cnt)