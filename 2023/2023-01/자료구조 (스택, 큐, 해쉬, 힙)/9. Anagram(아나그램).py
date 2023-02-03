import sys

input = sys.stdin.readline

# 1번 : 혼자 푼 것
# a = {chr(i): 0 for i in range(65, 91)}
# a.update({chr(j): 0 for j in range(97, 123)})

# for c in list(input().strip()):
#     a[c] += 1

# for s in list(input().strip()):
#     if a[s] == 0:
#         print("NO")
#         break
#     elif a[s] > 0:
#         a[s] -= 1
# else:
#     print("YES")

# ==============================================

# 2번 : 힌트 살짝 본 것
# s = dict()

# for x in input().strip():
#     s[x] = s.get(x, 0) + 1

# for x in input().strip():
#     if s.get(x, 0) - 1 == -1:
#         print("NO")
#         break
#     else:
#         s[x] -= 1
# else:
#     print("YES")

# ==============================================

# 3번 : 선생님 코드

# a = input().strip()
# b = input().strip()

# str1 = dict()
# str2 = dict()
# for x in a:
#     str1[x] = str1.get(x, 0) + 1
# for x in b:
#     str2[x] = str2.get(x, 0) + 1

# for i in str1.keys():
#     if i in str2.keys():
#         if str[i] != str[i]:
#             print("NO")
#             break
#     else:
#         print("NO")
#         break
# else:
#     print("YES")

# ==============================================

# 4번 : 리스트 해시 푼 것

li = [0] * 52

for c in input().strip():
    o = ord(c)
    print(o)
    if 65 <= o <= 90:
        li[o-65] += 1
    # elif 97 <= o <= 122:
    else:
        li[o-71] += 1

for x in input().strip():
    o = ord(x)
    if 65 <= o <= 90:
        if li[o-65] == 0:
            print("NO")
            break
        li[o-65] -= 1
    # elif 97 <= o <= 122:
    else:
        if li[o-71] == 0:
            print("NO")
            break
        li[o-71] -= 1
else:
    print("YES")
