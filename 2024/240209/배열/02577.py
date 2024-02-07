# 02577 숫자의 개수

import sys

ans = 1
anslist = [0] * 10
for n in sys.stdin.read().splitlines():
  ans *= int(n)
for c in str(ans):
  anslist[int(c)] += 1

print(*anslist, sep="\n")