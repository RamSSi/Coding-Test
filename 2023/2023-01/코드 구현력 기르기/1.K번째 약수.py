import sys

input = sys.stdin.readline

N, K = map(int, input().split())
order = 0

for i in range(N, 0, -1):
    if N % i == 0:
        order += 1
        if order == K:
            print(N // i)
            break
    # if i == 1 and order < K:
    #     print(-1)
else:
    print(-1)
