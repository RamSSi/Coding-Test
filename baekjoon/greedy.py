# 14916
# n = int(input())
# cnt = 0
# while n >= 0:
#     if (n == 1 or n == 3):
#         print("-1")
#         break
#     if n % 5 == 0:
#         cnt += (n // 5)
#         print(cnt)
#         break
#     else:
#         cnt += 1
#         n -= 2


# 2217
# import sys
# n = int(input())
# w = list(int(sys.stdin.readline().strip()) for _ in range(n))
# w.sort(reverse=True)
# for i in range(len(w)):
#     w[i] *= i+1
# print(max(w))


# 13305
# import sys
# n = int(input())
# result = 0
# min = 0
# dist = list(map(int, sys.stdin.readline().split()))
# perL = list(map(int, sys.stdin.readline().split()))
# if (sum(perL) == n):
#     print(perL[0] * sum(dist))
# else:
#     for i in range(n-1):
#         if perL[min] > perL[i]: min = i
#         result+= perL[min] * dist[i]
#     print(result)


# 1758
# import sys
# n = int(input())
# li = list(int(sys.stdin.readline().strip()) for _ in range(n))
# li.sort(reverse=True)
# result = 0
# for i in range(len(li)):
#     # if li[i]+1 <= (i+1):
#     #     li[i] = 0
#     # else:
#     #     li[i] = li[i] + 1 - (i+1)
#     tip = li[i] - i
#     if tip > 0:
#         result += tip
# print(result)


# 11508
# import sys
# n = int(input())
# li = list(int(sys.stdin.readline().strip()) for _ in range(n))
# li.sort(reverse=True)
# result = 0
# a = 0
# if n < 3:
#     result = sum(li)
# else:
#     for i in range(0, n - (n % 3), 3):
#         result += (li[i] + li[i+1])
#         a = i
#     if (n % 3 != 0):
#         a += 3
#         for i in range(n % 3):
#             result += li[a+i]
# # cnt_3 = 1
# # for i in li:
# #     if cnt_3 == 3:
# #         cnt_3 = 1
# #         continue
# #     result += i
# #     cnt_3 += 1
# # print(result)


# 11399
# import sys
# n = int(input())
# li = list(map(int, sys.stdin.readline().split()))
# li.sort()
# result = 0
# for i in range(n):
#     result += sum(li[:i+1])
# print(result)


# 20115
# import sys
# n = int(input())
# li = list(map(int, sys.stdin.readline().split()))
# li.sort()
# result = li[n-1]
# for i in range(n-1):
#     result += li[i]/2
# print(result)



# # 1018 : 체스판 다시 칠하기
# import sys
# R, C = map(int, input().split())
# chessboard = [sys.stdin.readline().strip() for _ in range(R)]

# def checkColor(chessboard, curR, curC, c):
#     color = ['B', 'W']
#     paint = 0
#     firstColor = color[c]
#     for i in range(curR, curR+8):
#         for j in range(curC, curC+8):
#             if chessboard[i][j] != firstColor:
#                 paint += 1
#             if j == (curC + 7):
#                 continue
#             c = 1 if c == 0 else 0
#             firstColor = color[c]
#     return paint

# def checkChessboard(chessboard, R, C):
#     pMin = 64
#     for r in range(R-7):
#         for c in range(C-7):
#             cnt = min(checkColor(chessboard, r, c, 0), checkColor(chessboard, r, c, 1))
#             if cnt == 0:
#                 return cnt
#             if pMin > cnt:
#                 pMin = cnt
#     return pMin

# print(checkChessboard(chessboard, R, C))

