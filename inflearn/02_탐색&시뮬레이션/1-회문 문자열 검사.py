# 대문자 소문자 구분하지 않으면 s.upper() 메소드를 이용해 대문자로 변환 후 코드를 짠다.

# import sys

# N = int(input())

# for i in range(N):
#     s = list(sys.stdin.readline().strip())
#     for i in range(len(s)//2):
#         if s[i] == s[-1] or abs(ord(s[i]) - ord(s[-1])) == 32:
#             s.pop()
#         else:
#             print("NO")
#             break
#     else:
#         print("YES")

import sys

N = int(input())

for _ in range(N):
    s = (sys.stdin.readline().strip()).upper()
    s = list(s)
    if s == s[::-1]:
        print("NO")
    else:
        print("YES")
