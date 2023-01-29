import sys

input = sys.stdin.readline

m = list(input().strip())

stack = []
res = ""

for x in m:
    if x.isdecimal():
        res += x
    else:
        if x == "(":
            stack.append(x)
        elif x in "*/":
            while stack and stack[-1] in "*/":
                res += stack.pop()
            stack.append(x)
        elif x in "+-":
            while stack and stack[-1] != "(":
                res += stack.pop()
            stack.append(x)
        elif x == ")":
            while stack and stack[-1] != "(":
                res += stack.pop()
            stack.pop()
while stack:
    res += stack.pop()
print(res)

# res = []
# for i in range(len(m)):
#     if m[i].isdecimal():
#         res.append(m[i])
#         if i == 0:
#             continue
#         if stack[-1] in ["*", "/"]:
#             res.append(stack.pop())
#     elif m[i] == ")":
#         while stack[-1] != "(":
#             res.append(stack.pop())
#         stack.pop()
#         if stack and stack[-1] in ["*", "/"]:
#             res.append(stack.pop())
#     else:
#         stack.append(m[i])
# while stack:
#     res.append(stack.pop())


print("".join(res))
