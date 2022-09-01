import sys
input = sys.stdin.readline

def Count():
    print()

N = int(input())
rev = list(map(int, input().split()))
ori = [0] * N

for i in range(1, N+1):
    for j in range(N):
        if rev[i] == 0 and ori[j] == 0:
            ori[j] = i + 1
            break
        elif ori[j] == 0:
            rev[i] -= 1
print(*ori, sep=' ')

# for n in range(1, N+1):
#     cnt = 0
#     for i in range(N):
#         if ori[i] == 0:
#             cnt += 1
#         if cnt > rev[n - 1]:
#             ori[i] = n
#             break
# print(*ori, sep=' ')