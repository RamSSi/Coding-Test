import sys

input = sys.stdin.readline

stick = list(input().strip())
print(stick)
stack = []
cnt = 0
res = 0
prev = '0'
for i in stick:
    if i == '(' and prev == ')':
        res += cnt
    elif prev == ')':
        cnt -= 1
        res += 1
    
    if prev == '(':
        cnt += 1
    print(prev, i, cnt, res)
    prev = i

print(cnt)