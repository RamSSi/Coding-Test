import sys
from collections import deque

input = sys.stdin.readline

req = list(input().strip())
N = int(input())

for i in range(N):
    r = deque(req)
    for l in list(input().strip()):
        if l == r[0]:
            r.popleft()
        if len(r) == 0:
            print("#%d YES" % (i+1))
            break
    if r:
        print("#%d NO" % (i+1))
