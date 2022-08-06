# # 2606
# import sys

# c = int(input())
# clink = [[] for _ in range(c+1)]
# visited = [False]*(c+1)
# for _ in range(int(input())) :
#     a, b = map(int, sys.stdin.readline().split())
#     clink[a].append(b)
#     clink[b].append(a)

# def dfs(v):
#     visited[v] = True
#     for i in clink[v]:
#         if not visited[i]:
#             dfs(i)
# dfs(1)
# print(visited.count(True)-1)

# from collections import deque
# import sys

# def appendInput(graph):
#     a, b = map(int, sys.stdin.readline().split())
#     graph[a].append(b)
#     graph[b].append(a)

# def bfs(start, visited, cnt):
#     queue = deque([start])
#     visited[start] = True
#     while(queue):
#         v = queue.popleft()
#         for i in graph[v]:
#             if not visited[i]:
#                 visited[i] = True
#                 cnt += 1
#                 queue.append(i)
#     return cnt

# N = int(sys.stdin.readline())
# M = int(sys.stdin.readline())
# graph = [[] for _ in range(N+1)]
# visited = [False] * (N+1)
# for i in range(M):
#     appendInput(graph)
# print(bfs(1, visited, 0))



# 1260
# from collections import deque
# import sys

# def dfs(v, visited):
#     visited[v] = True
#     print(v, end=" ")
#     for i in graph[v]:
#         if not visited[i]:
#             dfs(i, visited)

# def bfs(start, visited):
#     queue = deque([start])
#     while queue:
#         v = queue.popleft()
#         print(v, end=" ")
#         visited[v] = True
#         for i in graph[v]:
#             if not visited[i]:
#                 queue.append(i)
#                 visited[i] = True

# n, m, v = map(int, input().split())
# graph = [[] for _ in range(n + 1)]
# for _ in range(m):
#     a, b = map(int, sys.stdin.readline().split())
#     graph[a].append(b)
#     graph[b].append(a)
# for i in range(n+1):
#     graph[i].sort()
# visited = [False] * (n+1)
# dfs(v, visited)
# print()
# visited = [False] * (n+1)
# bfs(v, visited)

# from collections import deque
# import sys

# def dfs(graph, v, visited):
#     visited[v] = True
#     print(v, end=" ")
#     for i in graph[v]:
#         if not visited[i]:
#             dfs(graph, i, visited)

# def bfs(graph, start, visited):
#     queue = deque([start])
#     visited[start] = True
#     while(queue):
#         v = queue.popleft()
#         print(v, end=" ")
#         for i in graph[v]:
#             if not visited[i]:
#                 queue.append(i)
#                 visited[i] = True

# def sortGraph(N, graph):
#     for i in range(1, N+1):
#         graph[i].sort()

# def inputGraph(M, graph):
#     for _ in range(M):
#         a, b = map(int, sys.stdin.readline().split())
#         graph[a].append(b)
#         graph[b].append(a)
    
# N, M, V = map(int, input().split())
# graph = [[] for _ in range(N+1)]
# visited1 = [False] * (N+1)
# visited2 = [False] * (N+1)
# inputGraph(M, graph)
# sortGraph(N, graph)
# dfs(graph, V, visited1)
# print()
# bfs(graph, V, visited2)



# # 11725
# # from collections import deque
# # import sys

# # def bfs(start, parentNode):
# #     queue = deque([start])
# #     parent[start] = 1
# #     while queue:
# #         v = queue.popleft()
# #         parentNode = v
# #         for i in graph[parentNode]:
# #             if not parent[i]:
# #                 queue.append(i)
# #                 parent[i] = parentNode


# # N = int(input())

# # graph = [[] for _ in range(N + 1)]
# # parent = [0] * (N + 1)
# # for _ in range(N - 1):
# #     a, b = map(int, sys.stdin.readline().split())
# #     graph[a].append(b)
# #     graph[b].append(a)
# # bfs(1, 0)
# # print(*parent[2:], sep="\n")

# from collections import deque
# import sys
# N = int(input())
# graph = [[] for _ in range(N + 1)]
# parent = [0] * (N + 1)
# visited = [False] * (N + 1)
# def inputGraph(graph, N):
#     for _ in range(N-1):
#         a, b = map(int, sys.stdin.readline().split())
#         graph[a].append(b)
#         graph[b].append(a)

# # def dfs(graph, v, visited, parent):
# #     visited[v] = True
# #     for i in graph[v]:
# #         if not visited[i]:
# #             parent[i] = v
# #             dfs(graph, i, visited, parent)

# def bfs(graph, start, visited, parent):
#     queue = deque([start])
#     visited[start] = True
#     while(queue):
#         v = queue.popleft()
#         for i in graph[v]:
#             if not visited[i]:
#                 queue.append(i)
#                 parent[i] = v
#                 visited[i] = True

# inputGraph(graph, N)
# bfs(graph, 1, visited, parent)
# print(*parent[2:], sep="\n")



# # 1325 : 효율적인 해킹
# from collections import deque
# import sys

# def bfs(graph, start, N):
#     flag = [False] * (N + 1)
#     queue = deque([start])
#     flag[start] = True
#     cnt = 1
#     while(queue):
#         v = queue.popleft()
#         for i in graph[v]:
#             if not flag[i]:
#                 queue.append(i)
#                 flag[i] = True
#                 cnt += 1
#     return cnt

# N, M = map(int, input().split())
# arr = [[] for _ in range(N+1)]
# for i in range(M):
#     a, b = map(int, sys.stdin.readline().split())
#     arr[b].append(a)

# maxHack = 0
# maxlist = []
# for i in range(1, N+1):
#     result = bfs(arr, i, N)
#     if maxHack > result:
#         continue
#     elif maxHack == result:
#         maxlist.append(i)
#     else:
#         maxHack = result
#         maxlist = [i]

# print(*maxlist, sep=" ")



# # # 2178
# # import sys
# # N, M = map(int, input().split())
# # hack = [[] for _ in range(N+1)]
# # curr_visited = set()
# # for _ in range(M):
# #     a, b = map(int, sys.stdin.readline().split())
# #     hack[b].append(a)
# # visit = [0] * (N+1)
# # global n

# # def dfs(v):
# #     curr_visited.add(v)
# #     global n
# #     n += 1
# #     for i in hack[v]:
# #         if i not in curr_visited:
# #             dfs(i)

# # for i in range(1, N+1):
# #     n = 0
# #     dfs(i)
# #     visit[i] = n
# #     curr_visited = set()
# # k = max(visit)
# # print(*list(filter(lambda i: visit[i] == k, range(1, N+1))))

# import math
# import time
# import sys
# from collections import deque
# N, M = map(int, input().split())

# maze = [list(sys.stdin.readline().strip()) for _ in range(N)]
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# def minShift(maze, N, M):
#     maze[0][0] = 1
#     queue = deque()
#     queue.append((0, 0))
#     while queue:
#         x, y = queue.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if nx < 0 or ny < 0 or nx > (N-1) or ny > (M-1):
#                 continue
#             if maze[nx][ny] == '1':
#                 maze[nx][ny] = maze[x][y] + 1
#                 queue.append((nx, ny))
#     print(maze[N-1][M-1])

# minShift(maze, N, M)



# 2178

# import sys
# from collections import deque
# N, M = map(int, input().split())

# maze = [list(sys.stdin.readline().strip()) for _ in range(N)]
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# def minShift(maze, N, M):
#     maze[0][0] = 1
#     queue = deque()
#     queue.append((0, 0))
#     while queue:
#         x, y = queue.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if nx < 0 or ny < 0 or nx > (N-1) or ny > (M-1):
#                 continue
#             if maze[nx][ny] == '1':
#                 maze[nx][ny] = maze[x][y] + 1
#                 queue.append((nx, ny))
#     print(maze[N-1][M-1])

# minShift(maze, N, M)



# 2667
# import sys

# N = int(input())
# exist = [list(sys.stdin.readline().strip()) for _ in range(N)]

# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
# cnt = []
# global n
# n = 0
# def complex(x, y):
#     global n
#     if x < 0 or y < 0 or x > (N-1) or y > (N-1):
#         return False

#     if exist[x][y] == '1':
#         exist[x][y] = n + 1
#         complex(x-1, y)
#         complex(x+1, y)
#         complex(x, y-1)
#         complex(x, y+1)
#         n = n + 1

# for i in range(N):
#     for j in range(N):
#         complex(i, j)
#         if n > 0: cnt.append(n)
#         n = 0
# print(len(cnt))
# cnt.sort()
# print(*cnt, sep="\n")



# # # 16918 : 봄버맨
# import sys
# R, C, N = map(int, sys.stdin.readline().split())
# graph = [list(sys.stdin.readline().strip()) for _ in range(R)]

# def bomb(graph, N):
#     if N == 1:
#         return graph
#     elif N % 2 == 0:
#         return list(['O' for _ in range(C)] for _ in range(R))
#     elif N % 4 == 3:
#         graph2 = list(['O' for _ in range(C)] for _ in range(R))
#         bombArr = []
#         xArr = [0, 0, 0, 1, -1]
#         yArr = [0, 1, -1, 0, 0]
#         for i in range(R):
#             for j in range(C):
#                 if graph[i][j] == 'O':
#                     bombArr.append((i, j))
#         for (x, y) in bombArr:
#             for i in range(5):
#                 nx = x + xArr[i]
#                 ny = y + yArr[i]
#                 if (nx < 0 or ny < 0 or nx == R or ny == C):
#                     continue
#                 graph2[nx][ny] = '.'
#         return graph2
#     elif N != 1 and N % 4 == 1:
#         graph3 = bomb(graph, 3)
#         return bomb(graph3, 3)
        
# graph_result = bomb(graph, N)
# for i in graph_result:
#     print(*i, sep="")



# # 7576 : 토마토
# import sys
# from collections import deque
# M, N = map(int, sys.stdin.readline().split())
# field = [list(sys.stdin.readline().split()) for _ in range(N)]
# ripe = []
# all = N * M
# order = 100

# def checkRipe(N, M, cnt):
#     for i in range(N):
#         for j in range(M):
#             if field[i][j] == '1':
#                 ripe.append((i, j))
#                 field[i][j] = 100
#             elif field[i][j] == '-1':
#                 if N == 1:
#                     cnt = -100
#                     break
#                 cnt -= 1
#     return cnt

# def ripen(ripe, order, cnt):
#     xx = [-1, 1, 0, 0]
#     yy = [0, 0, 1, -1]
#     cnt -= len(ripe)
#     while(ripe):
#         store = []
#         order += 1
#         for (x, y) in ripe:
#             for n in range(4):
#                 nx = x + xx[n]
#                 ny = y + yy[n]
#                 if (nx == N or ny == M or nx < 0 or ny < 0):
#                     continue
#                 if field[nx][ny] == '0':
#                     field[nx][ny] = order
#                     store.append((nx, ny))
#                     cnt -= 1
#         ripe = store
#     return cnt, order-101


# cnt = checkRipe(N, M, all)
# cnt, result = ripen(ripe, order, cnt)

# if cnt == 0:
#     print(result)
# else:
#     print(-1)



# # 14502 : 연구소
# import sys
# from itertools import combinations
# from collections import deque

# def view():
#     empty, birus = [], []
#     for i in range(N):
#         for j in range(M):
#             if field[i][j] == '0':
#                 empty.append((i, j))
#             elif field[i][j] == '2':
#                 birus.append((i, j))
#     return empty, birus

# def setWall(comb):
#     for r, c in comb:
#         field[r][c] = '1'

# def collapseWall(comb):
#     for r, c in comb:
#         field[r][c] = '0'

# dir = [(1, 0), (-1, 0), (0, -1), (0, 1)]
# def bfs(safe, virus):
#     visited = [[False] * M for _ in range(N)]
#     queue = deque(virus)
#     while(queue):
#         r, c = queue.popleft()
#         for dr, dc in dir:
#             nr, nc = r + dr, c + dc
#             if (0 <= nr < N) and (0 <= nc < M):
#                 if field[nr][nc] == '0' and not visited[nr][nc]:
#                     visited[nr][nc] = True
#                     queue.append((nr, nc))
#                     safe -= 1
#     return safe

# N, M = map(int, input().split())
# field = [list(sys.stdin.readline().split()) for _ in range(N)]


# empty, virus = view()
# combs = combinations(empty, 3)

# cnt = 0
# safe = len(empty) - 3
# for comb in combs:
#     setWall(comb)

#     currSafe = bfs(safe, virus)
    
#     if currSafe > cnt:
#         cnt = currSafe
    
#     collapseWall(comb)

# print(cnt)



# # 7569 : 토마토
# import sys

# def searchRipe(all, cnt):
#     ripe = []
#     for h in range(H):
#         for n in range(N):
#             for m in range(M):
#                 if field[h][n][m] == '1':
#                     field[h][n][m] = cnt
#                     ripe.append((h, n, m))
#                     all -= 1
#                 elif field[h][n][m] == '-1':
#                     all -= 1
#     return all, cnt, ripe

# def ripen(ripe, all, cnt):
#     dirs = [(0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0)]
#     while(ripe):
#         store = []
#         cnt += 1
#         for h, n, m in ripe:
#             for dh, dn, dm in dirs:
#                 hh = h + dh
#                 nn = n + dn
#                 mm = m + dm
#                 if 0 <= hh < H and 0 <= nn < N and 0 <= mm < M and field[hh][nn][mm] == '0':
#                     field[hh][nn][mm] = cnt
#                     store.append((hh, nn, mm))
#                     all -= 1
#         ripe = store
#     cnt -= 101
#     return all, cnt

# M, N, H = map(int, input().split())
# field= [list() for _ in range(H)]
# for i in range(H):
#     field[i] = list(sys.stdin.readline().split() for _ in range(N))
# all = N * M * H
# cnt = 100

# all, cnt, ripe = searchRipe(all, cnt)
# all, cnt = ripen(ripe, all, cnt)

# if all == 0:
#     print(cnt)
# else:
#     print(-1)



# 2636 : 치즈
import sys
from collections import deque
R, C = map(int, input().split())
plate = list([sys.stdin.readline().split()] for _ in range(R))
cheese = list()
air = []

for i in range(C):
    air.append((0, i))
    air.append((R-1, i))
for i in range(1, R-1):
    air.append((i, 0))
    air.append((i, C-1))

dirs = [(1, 0), (-1, 0), (0, -1), (0, 1)]

def setOut():
    queue = deque(air)
    while(queue):
        r, c = queue.popleft()
        plate[r][c] = 0
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < R and 0 <= nc < C:
                if plate[nr][nc] == '0':
                    queue.append((nr, nc))
                    plate[nr][nc] = 0
                elif plate[nr][nc] == '1':
                    cheese.append((nr, nc))
                    plate[nr][nc] = 1

def melt():
    queue = deque(cheese)
    while(queue):
        r, c = queue.popleft()
        plate[r][c] = 0
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < R and 0 <= nc < C:
                if plate[nr][nc] == '1':
                    queue.append((nr, nc))
                    plate[nr][nc] = 1