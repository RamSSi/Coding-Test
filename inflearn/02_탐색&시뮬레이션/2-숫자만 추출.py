# import sys, re

# p = re.compile("[0-9]")

# s = input()
# n = ''
# for i in s:
#     if p.match(i):
#         n += i
# n = int(n)

# cnt = 1
# for i in range(1, n):
#     if n % i == 0:
#         cnt += 1
# print(n)
# print(cnt)

import sys

s = input()
res = 0
for x in s:
    if x.isdemical():
        res = res * 10 + int(x)
print(res)

cnt = 0
for i in range(1, res + 1):
    if res % 1 == 0:
        cnt += 1
print(cnt)