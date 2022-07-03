from collections import deque
# graph = [
#     [],
#     [2, 3, 8],
#     [1, 7],
#     [1, 4, 5],
#     [3, 5],
#     [3, 4],
#     [7],
#     [2, 6, 8],
#     [1, 7],
# ]


# # dfs
# def dfs(graph, v, visited):
#     visited[v] = True
#     print(v, end=" ")
#     for i in graph[v]:
#         if visited[i] == False:
#             dfs(graph, i, visited)


# visited_dfs = [False] * 9
# dfs(graph, 1, visited_dfs)

## bfs


# def bfs(graph, v, visited):
#     queue = deque([v])
#     visited[v] = True
#     while queue:
#         visit = queue.popleft()
#         print(visit, end=" ")
#         for i in graph[visit]:
#             if visited[i] == False:
#                 queue.append(i)
#                 visited[i] = True


# visited_bfs = [False] * 9
# bfs(graph, 1, visited_bfs)





# 인접 행렬로도 dfs 만들어보기
INF = 99
graph_matrix = [
    [],
    [INF, 0, 1, 1, INF, INF, INF, INF, 1],
    [INF, 1, 0, INF, INF, INF, INF, 1, INF],
    [INF, 1, INF, 0, 1, 1, INF, INF, INF],
    [INF, INF, INF, 1, 0, 1, INF, INF, INF],
    [INF, INF, INF, 1, 1, 0, INF, INF, INF],
    [INF, INF, INF, INF, INF, INF, 0, 1, INF],
    [INF, INF, 1, INF, INF, INF, 1, 0, 1],
    [INF, 1, INF, INF, INF, INF, INF, 1, 0]
]

visited_matrix = [False] * 9
print(visited_matrix)

def dfs_matrix(graph, v, visited):
    visited[v] = True
    print(visited)
    print("방문순서 : ", v)
    for i in range(9):
        if graph[v][i] == 1 and not visited[i]:
            dfs_matrix(graph, i, visited)
dfs_matrix(graph_matrix, 1, visited_matrix)