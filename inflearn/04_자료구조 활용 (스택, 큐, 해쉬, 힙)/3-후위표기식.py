import sys
from tkinter import W
input = sys.stdin.readline

ex = list(input().strip())

stack = []
res = []

for ch in ex:
    if ch.isdecimal():
        res += ch
    else:
        if ch in '+-':
            while stack and stack[-1] != '(':
                res += stack.pop()
            stack.append(ch)
        elif ch in '*/':
            while stack and stack[-1] in '*/':
                res += stack.pop()
            stack.append(ch)
        elif ch == '(':
            stack.append(ch)
        elif ch == ')':
            while stack[-1] != '(':
                res += stack.pop()
            stack.pop()

while stack:
    res += stack.pop()

print(*res, sep='')