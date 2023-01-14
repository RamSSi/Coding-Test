# import sys
# import math

# N = int(input())
# nlist = list(map(str, sys.stdin.readline().split()))

# for i in nlist:
#     rev = int("".join(reversed(i)))
#     last = math.floor(rev / 2) + 1
#     for j in range(2, last):
#         if rev % j == 0:
#             break
#     if j == last - 1:
#         print(rev, end=' ')

import sys

def reverse(s):
    n = 0
    for i in range(len(s)):
        n += int(s[i]) * (10 ** i)
    return n

def isPrime(n):
    if n == 1:
        return False
    for i in range(2, n//2):
        if n % i == 0:
            return False
    else:
        return True

N = int(input())
nlist = list(sys.stdin.readline().split())
for n in nlist:
    n = reverse(n)
    if isPrime(n):
        print(n, end = ' ')