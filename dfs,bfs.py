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


# 