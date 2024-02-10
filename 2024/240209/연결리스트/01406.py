# 01406 에디터

s = list(input())
c = len(s)
for _ in range(int(input())):
    i = input().split()
    if i[0] == 'L' and c != 0:
        c -= 1
    elif i[0] == 'D' and c != len(s):
        c += 1
    elif i[0] == 'B' and c != 0:
        s.pop(c-1)
        c -= 1
    elif i[0] == 'P':
        s.insert(c, i[1])
        c += 1

print(*s, sep='')

# ======================================
import sys
l = list(input())
r = []

for _ in range(int(input())):
    i = list(sys.stdin.readline().split())
    if i[0] == 'L' and l: r.append(l.pop())
    elif i[0] == 'D' and r: l.append(r.pop())
    elif i[0] == 'B' and l: l.pop()
    elif i[0] == 'P': l.append(i[1])

ans = l + r[::-1]
print(*ans, sep='')