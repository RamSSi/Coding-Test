import sys
import itertools

input = sys.stdin.readline

n = int(input())
mlist = []

for _ in range(n):
    s, f = map(int, input().split())
    mlist.append((s, f))
comb = []
for i in range(n, 0, -1):
    comb.append(list(itertools.combinations(range(n), i)))

print(comb)

def Count(comb):
    cnt = 0
    res = []
    print("시작", comb)
    for choice in comb:
        print(choice)
        if cnt == 0:
            res.append(mlist[choice])
            cnt = 1
            print(res)
            continue
        s, f = res[-1]
        cs, cf = mlist[i]
        if f <= cs:
            res.append((cs, cf))
            print(res)
            cnt += 1
    print(res)
    return cnt

cnt = 0
for i in range(n):
    for j in comb[i]:
        c = Count(j)
        if c > cnt:
            cnt = c
            if c == n:
                break
            
        
print(cnt)
    
