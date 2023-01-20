import sys

input = sys.stdin.readline

N = int(input())
nlist = list(map(int, input().split()))

sum = 0
cnt = 0

for num in nlist:
    if num == 1:
        cnt += 1
        sum += cnt
    else:
        cnt = 0

print(sum)
