import sys
A = int(input())
B = int(input())
C = int(input())
num = list(str(A * B * C))
nlist = [0] * 10

for i in num:
    nlist[int(i)] += 1

print(*nlist, sep='\n')