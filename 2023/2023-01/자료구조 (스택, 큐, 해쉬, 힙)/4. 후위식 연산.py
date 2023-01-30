import sys

input = sys.stdin.readline

s = list(input().strip())

res = 0
tmp = []

for x in s:
    if x.isdecimal():
        tmp.append(int(x))
    else:
        b = tmp.pop()
        a = tmp.pop()
        if x == "+":
            tmp.append(a+b)
        elif x == "-":
            tmp.append(a-b)
        elif x == "*":
            tmp.append(a*b)
        elif x == "/":
            tmp.append(a/b)

res = tmp.pop()

print(int(res))
