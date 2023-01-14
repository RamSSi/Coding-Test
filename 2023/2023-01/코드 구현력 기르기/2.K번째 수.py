import sys

input = sys.stdin.readline

for i in range(int(input())):
    N, s, e, k = map(int, input().split())
    nList = list(map(int, input().split()))[s-1:e]
    nList.sort()
    print("#%d %d" % (i+1, nList[k-1]))
