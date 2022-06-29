# 10950
# a = int(input())
# print(a)
# for i in range(a):
#     b, c = map(int, input().split());
#     print(b+c)


# 8393
# a = int(input())
# sum = 0
# for i in range(a):
#    sum += (i + 1)
# print(sum)


# 15552
from math import perm
import sys
from xml.dom.minidom import CharacterData

# a = int(input())
# for i in range(a):
#     b, c = map(int, sys.stdin.readline().split())
#     print(b+c)


# 11021
# a = int(input())
# for i in range(a):
#     b, c = map(int, sys.stdin.readline().split())
#     str = 'Case #{0}: {1}'.format(i+1, b+c)
#     print(str)


# 11022
# a = int(input());
# for i in range(a):
#     b, c = map(int, sys.stdin.readline().split())
#     print("Case #{}: {} + {} = {}".format(i+1, b, c, b+c))


# 2438
# a = int(input())
# for i in range(a):
#     for j in range(i+1):
#         print('*', end='')
#     print()


# 2439
# a = int(input())
# for i in range(1, a+1):
#     for j in range(a - i):
#         print(' ', end='')
#     for k in range(i):
#         print('*', end='')
#     print()


# 1152
# a = sys.stdin.readline().split()
# print(len(a))


# 1157
# word = input().lower()
# word_list = list(set(word))
# cnt = []

# for i in word_list:
#     count = word.count(i)
#     cnt.append(count)

# if (cnt.count(max(cnt)) >= 2): print("?")
# else: print(word_list[(cnt.index(max(cnt)))].upper())


# 1330
# a, b = map(int, input().split())
# if (a < b): print("<")
# elif (a > b): print(">")
# else: print("==")


# 1546
# a = int(input())
# alist = list(map(int, sys.stdin.readline().split()))
# newlist = []
# for score in alist:
#     newlist.append(score/max(alist) * 100)
# print(sum(newlist)/a)


# 2475
# alist = list(map(int, sys.stdin.readline().split()))
# sum = 0
# for i in alist:
#     sum += i**2
# print(sum%10)


# 2562
# import sys
# alist = [int(sys.stdin.readline().strip()) for _ in range(9)]
# print(max(alist))
# print(alist.index(max(alist))+1)


# 2577
# mul = 1
# for _ in range(3):
#     mul *= int(input())
# strlist = list(str(mul))
# for i in range(10):
#     print(strlist.count(str(i)))


# 빈 칸을 기준으로 나눌 땐 split(), 개행문자 기준으로 나눌 땐 strip()


# 2675
# t = int(input())
# for _ in range(t):
#     num, s = input().split()
#     text = ''
#     for i in s:
#         text += i*int(num)
#     print(text)


# 2908
# a, b = map(reversed, input().split())
# a = "".join(list(a))
# b = "".join(list(b))

# print(a) if (a > b) else print(b)


# 2920
# clist = list(map(int, input().split()))
# a = [1,2,3,4,5,6,7,8]
# b = [8,7,6,5,4,3,2,1]
# if (clist == a): print("ascending")
# elif (clist==b): print("descending")
# else: print("mixed")


# 8958
# n = int(input())
# for _ in range(n):
#     result = 0
#     add = 0
#     li = sys.stdin.readline()
#     for i in range(len(li)):
#         if i == 0:
#             if li[i] == 'O':
#                 add += 1
#                 result += add
#         else:
#             if li[i] == 'O':
#                 if li[i-1] == 'O':
#                     add += 1
#                     result += add
#                 else:
#                     add += 1
#                     result += 1
#             else:
#                 add = 0
#     print(result)


# 9498
# score = int(input())
# print("A") if score >= 90 else (print("B") if score >= 80 else (print("C") if score >= 70 else (print("D") if score >= 60 else (print("F")))))


# 10809
# s = list(input())
# li = [-1]*26
# s_set = set(s)
# for ch in s_set:
#     li[ord(ch)-97] = s.index(ch)
# for i in li:
#     print(i, end=' ')


# 10818
# import sys
# n = int(input())
# nlist = list(map(int, sys.stdin.readline().split()))
# print(f"{min(nlist)} {max(nlist)}")


# 10871
# n, x = map(int, input().split())
# nlist = list(map(int, sys.stdin.readline().split()))
# nlist = list(map(str, filter(lambda i: i < x, nlist)))
# print(' '.join(nlist))

# # a,b = map(int,input().split())
# # score = [x for x in input().split() if int(x)<b]
# # print(' '.join(score))


# 10950
# for i in range(int(input())):
#     a, b = map(int, input().split())
#     print(a+b)


# 10951
# for i in sys.stdin.readlines(): # 모든 입력 line을 한 번에 받기
#     a, b = map(int, i.split())  # 한 라인마다 공백으로 구분하여 a,b에 넣기
#     print(a + b)


# 10952
# import sys
# while True:
#     a, b = map(int, sys.stdin.readline().split())
#     if a==0 and b==0: break
#     print(a+b)


# 11720
# # from functools import reduce
# # input()
# # print(reduce(lambda acc, cur: acc + cur, map(int, list(input()))))

# input()
# sum = 0
# for i in list(map(int, list(input()))):
#     sum+=i
# print(sum)


# 1085
# x, y, w, h = map(int, input().split())
# print(min([x, y, w-x, h-y]))


# 1259
# import sys
# import math
# def calc(a):
#     for i in range(math.ceil(len(a)/2)):
#         if (a[i] == a[-i-1]):
#             if i == math.ceil(len(a)/2)-1:
#                 print("yes")
#             continue
#         else:
#             print("no")
#             break
# while True:
#     a = list(sys.stdin.readline().rstrip())
#     if (a == ['0']): break
#     calc(a)


# 2231
# n = int(input())
# result=0
# for i in range(max(0, n-100, n-1000), n+1):
#     if i + sum(list(map(int, str(i)))) == n:
#         result = i
#         break
# print(result)


# 2292
# a = 1
# cnt = 1
# n = int(input())
# if (n == 1): cnt = 1
# else:
#     while True:
#         a += 6 * cnt
#         cnt += 1
#         if a >= n:
#             break
# print(cnt)


# 1271
# n, m = map(int, input().split())
# print(n//m, n%m)


# 2338
# import sys
# li = [int(sys.stdin.readline()) for _ in range (2)]
# print(li[0]+li[1],li[0]-li[1],li[0]*li[1])


# 2420
# from functools import reduce
# print(abs(reduce(lambda prev, curr: prev - curr, list(map(int, input().split())))))


# 2558
# import sys
# print(sum([int(sys.stdin.readline()) for _ in range (2)]))


# 2738
# m, n = map(int, input().split())
# a = []
# b = []
# for i in range(m):
#     a.append([sys.stdin.readline().split() for _ in range(n)])

# for i in range(m):
#     b.append([sys.stdin.readline().split() for _ in range(n)])
# print(i for i in a+b)


# 2743
# print(len(list(input())))


# 2744
# print(*list(map(lambda x: x.lower() if ord(x) < 97 else x.upper() if ord(x) >= 97 else 0, list(input()))), sep='')


# 2754


# 3003
# right = [1, 1, 2, 2, 2, 8]
# a = list(map(int, input().split()))
# for i in range(len(a)):
#     a[i] = right[i] - a[i]
# print(*a)


# 1264
# import sys
# a = 0
# cnt = 0
# str_list = ["A", "E", "I", "O", "U"]
# while True:
#     a = sys.stdin.readline().upper().strip()
#     if a == "#": break
#     for i in str_list:
#         cnt += a.count(i)
#     print(cnt)
#     cnt = 0


# 2440
# a = int(input())
# for i in range(a): print(*["*"*(a-i)])


# 2530
# a, b, c = map(int, input().split())
# d = int(input())
# a += d // 3600
# d -= d // 3600 * 3600
# b += d // 60
# d -= d // 60 * 60
# c += d
# if (c >= 60):
#     c -= 60
#     b += 1
# if (b >= 60):
#     b -= 60
#     a += 1
# if (a >= 24):
#     a %= 24
# print(a, b, c)


# 2752
# a = list(map(int, input().split()))
# a.sort()
# print(*a)


# 1247
# import sys
# for _ in range(3):
#     n = int(input())
#     a = []
#     result = 0
#     for _ in range(n):
#         a.append(int(sys.stdin.readline()))
#     result = sum(a)
#     print("0" if result == 0 else "-" if result < 0 else "+")


# from sys import stdin
# for _ in range(3):
#     N = int(stdin.readline())
#     li = [int(stdin.readline()) for i in range(N)]
#     if sum(li) == 0:
#         print("0")
#     elif sum(li) > 0:
#         print("+")
#     else:
#         print("-")


# 1267
# n = int(input())
# y=0
# m=0
# a = list(map(int, sys.stdin.readline().split()))
# for i in a:
#     y += (i // 30 + 1)*10
#     m += (i // 60 + 1)*15
# print("M " + str(m) if y > m else "Y " + str(y) if y < m else "Y M " + str(y))


# 1284
# import sys
# while True:
#     p = 2
#     n = list(sys.stdin.readline().strip())
#     if n == ['0']: break
#     p += len(n)-1
#     for i in n:
#         if i == '1': p += 2
#         elif i == '0': p += 4
#         else: p += 3
#     print(p)


# 1547
# import sys
# i = 1
# for _ in range(int(input())):
#     a, b = map(int, sys.stdin.readline().split())
#     if a == i:
#         i = b
#     elif b == i:
#         i = a
# print(i)


# 1598
# def wid(num):
#     if num % 4 != 0:
#         return num%4
#     else:
#         return 4
# def hei(num):
#     if num % 4 == 0:
#         return num // 4 - 1
#     else:
#         return num // 4
# a, b = map(int, input().split())
# distance = 0
# distance += abs(wid(a) - wid(b)) + abs(hei(a) - hei(b))
# print(distance)


# 1703
# import sys
# while True:
#   a = list(map(int, sys.stdin.readline().split()))
#   if len(a) == 1: break
#   cnt = 1
#   for i in range(1, a[0] * 2, 2):
#     cnt *= a[i]
#     cnt -= a[i+1]
#   print(cnt)


# 1837
# a, b = map(int, input().split())
# for i in range(2, b):
#   if a % i == 0:
#     a = 1
#     print(f"BAD {i}")
#     break
# if (a != 1): print("GOOD")


# 5717
# while True:
#   a = sum(list(map(int, input().split())))
#   if a > 0: print(a)
#   else: break


# 2446
# n = int(input())
# space = 0
# star = 2*n+1
# for i in range(2*n-1):
#   if i < n:
#     space = i
#     star -=2
#   else:
#     space -= 1
#     star += 2
#   print(" "*space, end="")
#   print("*"*star)


# 2442
# n = int(input())
# for i in range(n):
#     print(" "*(n-1-i), end="")
#     print("*"*(2*i+1))


# 23802
# n = int(input())
# print(*["@"*n]* (5*n-n), sep="\n")
# print(*["@"*5*n + "\n"] * (n-1) + ["@"*5*n], sep="")


# 23804
# n = int(input())
# print(*["@@@@@"*n]*n, sep="\n")
# print(*["@"*n]*(3*n),sep="\n")
# print(*["@@@@@"*n]*n, sep="\n")


# 14916
# n = int(input())
# cnt = 0
# while n >= 0:
#     if (n == 1 or n == 3):
#         print("-1")
#         break
#     if n % 5 == 0:
#         cnt += (n // 5)
#         print(cnt)
#         break
#     else:
#         cnt += 1
#         n -= 2


# 2217
# import sys
# n = int(input())
# w = list(int(sys.stdin.readline().strip()) for _ in range(n))
# w.sort(reverse=True)
# for i in range(len(w)):
#     w[i] *= i+1
# print(max(w))










# a = ['1', '2', '3', '4', '5']
# from itertools import permutations
# from itertools import combinations
# from itertools import product
# from itertools import combinations_with_replacement
# print(list(permutations(a, 3)))
# print("\n\n")
# print(list(combinations(a,3)))
# print()
# print("\n\n")
# print(list(product(a, repeat=3)))
# print()
# print("\n\n")
# print(list(combinations_with_replacement(a, 3)))
