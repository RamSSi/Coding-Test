# 2606
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


# 11725
# from collections import deque
# import sys

# def bfs(start, parentNode):
#     queue = deque([start])
#     parent[start] = 1
#     while queue:
#         v = queue.popleft()
#         parentNode = v
#         for i in graph[parentNode]:
#             if not parent[i]:
#                 queue.append(i)
#                 parent[i] = parentNode


# N = int(input())

# graph = [[] for _ in range(N + 1)]
# parent = [0] * (N + 1)
# for _ in range(N - 1):
#     a, b = map(int, sys.stdin.readline().split())
#     graph[a].append(b)
#     graph[b].append(a)
# bfs(1, 0)
# print(*parent[2:], sep="\n")


# 1325
import sys
N, M = map(int, input().split())
hack = [[] for _ in range(N+1)]
curr_visited = set()
for _ in range(M):
	a, b = map(int, sys.stdin.readline().split())
	hack[b].append(a)
visit = [0] * (N+1)
global n
def dfs(v):
	curr_visited.add(v)
	global n
	n += 1 
	for i in hack[v]:
		if i not in curr_visited:
			dfs(i)

for i in range(1, N+1):
	n = 0
	dfs(i)
	visit[i] = n
	curr_visited = set()
k = max(visit)
print(*list(filter(lambda i: visit[i] == k, range(1, N+1))))




# import math
# import time
# import sys
# from collections import deque

# N, M = map(int, input().split())
# graph = [[] for _ in range(N + 1)]
# start = time.time()
# for _ in range(M):
#     a, b = map(int, sys.stdin.readline().split())
#     graph[b].append(a)
# end = time.time()
# print(f"{end - start:.5f} sec")

# def bfs(start):
#     visited = [False] * (N + 1)
#     queue = deque([start])
#     visited[start] = True
#     while queue:
#         v = queue.popleft()
#         for i in graph[v]:
#             if not visited[i]:
#                 queue.append(i)
#                 visited[i] = True
#     return visited.count(True)

# num = []
# for i in range(N + 1):
#     num.append(bfs(i))

# k = num.index(max(num))
# result = [k]
# for i in range(k+1, N+1):
#     if num[i] == num[k]:
#         result.append(i)
# print(*result)


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
