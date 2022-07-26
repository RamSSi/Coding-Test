from operator import index
import sys

dir = ['L', 'R', 'U', 'D']
Y = [-1, 1, 0, 0]
X = [0, 0, -1, 1]

N = int(input())
dirList = list(sys.stdin.readline().split())

startX, startY= 1, 1
limitX, limitY = N, N


for i in range(len(dirList)):
    currX, currY = startX + Y[dir.index(dirList[i])], startY + X[dir.index(dirList[i])]
    if (currX == 0 or currY == 0 or currX > N or currY > N):
        continue
    startX, startY = currX, currY
print(startY, startX)
