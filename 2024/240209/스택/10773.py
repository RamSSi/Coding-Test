# 10773 제로

import sys

stack = []
for _ in range(int(input())):
    a = int(sys.stdin.readline())
    if a == 0:
        stack.pop()
    else:
        stack.append(a)
print(sum(stack))