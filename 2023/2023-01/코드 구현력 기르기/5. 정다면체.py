import sys

input = sys.stdin.readline

N, M = map(int, input().split())
pList = [0] * (N+M+1)
answerList = []
maxN = 0

for i in range(1, N+1):
    for j in range(1, M+1):
        pList[i + j] += 1

for i in range(1, N+M+1):
    if pList[i] > maxN:
        maxN = pList[i]
        answerList = [i]
    elif pList[i] == maxN:
        answerList.append(i)

answerList.sort()

for n in answerList:
    print(n, end=" ")
