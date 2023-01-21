import sys

input = sys.stdin.readline

N = int(input())
Nlist = list(map(int, input().split()))

M = int(input())
Mlist = list(map(int, input().split()))

# 1) sort() 사용
# res = Nlist + Mlist
# res.sort()

# print(res)


# 2) 직접 정렬
res = []
nCnt = 0
mCnt = 0
while True:
    if Nlist[nCnt] <= Mlist[mCnt]:
        res.append(Nlist[nCnt])
        nCnt += 1
    else:
        res.append(Mlist[mCnt])
        mCnt += 1
    if nCnt == N:
        res += Mlist[mCnt:]
        break
    elif mCnt == M:
        res += Nlist[nCnt:]
        break
print(res)

# 3
# 1 3 5
# 5
# 2 3 6 7 9
