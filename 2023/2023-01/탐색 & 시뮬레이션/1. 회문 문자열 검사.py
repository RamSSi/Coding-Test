import sys

input = sys.stdin.readline

# for i in range(int(input())):
#     s = input().lower().strip()
#     if s == s[::-1]:
#         print("#%d YES" % (i+1))
#     else:
#         print("#%d NO" % (i+1))


for i in range(int(input())):
    s = input().lower().strip()
    for j in range(len(s)//2):
        if s[j] != s[- j - 1]:
            print("#%d NO" % (i+1))
            break
    else:
        print("#%d YES" % (i+1))
