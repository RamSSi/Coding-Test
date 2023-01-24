import sys

input = sys.stdin.readline

N = int(input())
mList = []

for i in range(N):
    a, b = map(int, input().split())
    mList.append((a, b))

mList.sort(key=lambda x: (x[1], x[0]))

end = mList[0][1]
cnt = 1

for i in range(1, N):
    (a, b) = mList[i]
    if a >= end:
        end = b
        cnt += 1

print(cnt)
