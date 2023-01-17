import sys

input = sys.stdin.readline

N = int(input())
ch = [0] * (N+1)
cnt = 0

for i in range(2, N+1):
    if ch[i] == 0:
        cnt += 1
        for j in range(i+1, N+1):
            if j % i == 0:
                ch[j] += 1

print(ch, cnt)
