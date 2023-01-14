import sys

input = sys.stdin.readline

num, m = map(int, input().split())
num = list(str(num))

stack = []
delete = []
for i in num:
    n = int(i)
    while stack and stack[-1] < n and m > 0:
        stack.pop()
        m -= 1
    stack.append(n)
    if m == 0:
        break

print(stack[:-m])
