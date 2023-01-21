import sys

input = sys.stdin.readline

N = int(input())
apple = []
res = 0

for i in range(N):
    apple.append(list(map(int, input().split())))

# for i in range(N):
#     if i <= N // 2:
#         add = sum(apple[i][N//2-i:N//2+i+1])
#         print(N//2-i, N//2+i)
#         res += add
#     else:
#         add = sum(apple[i][i-N//2:N-i+2])
#         print(i-N//2, N-i+1)
#         res += add

start = end = N // 2
for i in range(N):
    print(i)
    for j in range(start, end + 1):
        res += apple[i][j]
    if i < N // 2:
        start -= 1
        end += 1
    else:
        start += 1
        end -= 1

print(res)
