import sys
input = sys.stdin.readline

N = int(input())
l = list(map(int, input().split()))
res = [0] * (N)

for i in range(N):
    print(i+1, l[i])
    cnt = 0
    for j in range(N):
        if cnt == l[i] and res[j] == 0:
            res[j] = i+1
            break
        if res[j] == 0:
            cnt += 1
for num in res:
    print(num, end=" ")
