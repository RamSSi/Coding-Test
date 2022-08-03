import sys

size = int(input())
a = list(map(int, sys.stdin.readline().split()))
a.sort()
N = int(input())
idx = 0
cnt = 0

if N in a:
    cnt = 0

else:
    if N < a[0]:
        cnt = N - 1
    else:
        for i in range(1, size):
            if a[i-1] < N < a[i]:
                if a[i-1]+1 == N:
                    cnt = a[i] - 1 - N
                elif a[i+1] - 1 == N:
                    cnt = N - (a[i] + 1)
                else:
                    A = N - (a[i-1] + 1)
                    B = a[i] - 1 - N
                    cnt = (A * B) + A + B

print(cnt)