import sys

input = sys.stdin.readline

# N = int(input())
# result = []

# def reverse(x):
#     return int("".join(list(x)[::-1]))

# def isPrime(x):
#     if x == 1:
#         return 0
#     for i in range(2, x//2 + 1):
#         if x % i == 0:
#             return 0
#     else:
#         return x

# for num in list(input().split()):
#     strN = reverse(num)
#     if isPrime(strN) != 0:
#         result.append(strN)

# for ans in result:
#     print(ans, end=" ")


def reverse(x):
    res = 0
    while x > 0:
        t = x % 10
        res = res * 10 + t
        x //= 10
    return res


def isPrime(x):
    if x == 1:
        return False
    for i in range(2, x//2+1):
        if x % i == 0:
            return False
    else:
        return True


n = int(input())
a = list(map(int, input().split()))
for x in a:
    tmp = reverse(x)
    if isPrime(tmp):
        print(tmp, end=" ")
