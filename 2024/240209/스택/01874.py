# 01874 스택 수열

import sys
c = 0
stack = [0]
res = []
n = int(input())

for _ in range(n):
    a = int(sys.stdin.readline())
    while a > c:
        c += 1
        stack.append(c)
        res.append("+")
    if a == stack[-1]:
        stack.pop()
        res.append("-")
    elif a < stack[-1]:
        res = ["NO"]
        break

print(*res, sep="\n")