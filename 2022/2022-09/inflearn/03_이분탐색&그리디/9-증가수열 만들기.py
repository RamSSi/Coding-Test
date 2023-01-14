import sys
input = sys.stdin.readline

N = int(input())
nlist = list(map(int, input().split()))

res= []
last = 0
lt = 0
rt = N-1
while lt <= rt:
    tmp = []
    if nlist[lt] > last:
        tmp.append((nlist[lt], "L"))
    if nlist[rt] > last:
        tmp.append((nlist[rt], "R"))
    tmp.sort()
    if len(tmp) == 0:
        break
    else:
        res.append(tmp[0][1])
        last = tmp[0][0]
        if tmp[0][1] == 'L':
            lt += 1
        else:
            rt -= 1
print(*res, sep="")