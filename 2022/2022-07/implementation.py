# # 이코테 예제 4-1

# from operator import index
# import sys

# dir = ['L', 'R', 'U', 'D']
# Y = [-1, 1, 0, 0]
# X = [0, 0, -1, 1]

# N = int(input())
# dirList = list(sys.stdin.readline().split())

# startX, startY= 1, 1
# limitX, limitY = N, N


# for i in range(len(dirList)):
#     currX, currY = startX + Y[dir.index(dirList[i])], startY + X[dir.index(dirList[i])]
#     if (currX == 0 or currY == 0 or currX > N or currY > N):
#         continue
#     startX, startY = currX, currY
# print(startY, startX)



# # 이코테 예제 4-2

# N = int(input())
# cnt = 0
# for h in range(N+1):
#     for m in range(60):
#         for s in range(60):
#             if '3' in str(h) + str(m) + str(s):
#                 cnt += 1
# print(cnt)



# # 이코테 구현 - 실전문제 : 왕실의 나이트
# position = list(input())
# c, r = ord(position[0]), int(position[1])   # a = 97

# shiftR = [-2, -2, 2, 2, -1, 1, -1, 1]
# shiftC = [-1, 1, -1, 1, -2, -2, 2, 2]

# cnt = 0
# for i in range(8):
#     nr = r + shiftR[i]
#     nc = c + shiftC[i]

#     if nr < 1 or nc < 97 or nr > 8 or nc > 104:
#         continue
#     cnt += 1
# print(cnt)



#
import sys

# 북: 0, 동: 1, 남:2, 서: 3
turnR = [0, 1, 0, -1]
turnC = [-1, 0, 1, 0]
N, M = map(int, input())
r, c, dir = map(int, input())
cnt = 0
game = list([sys.stdin.readline()] for _ in range(N))