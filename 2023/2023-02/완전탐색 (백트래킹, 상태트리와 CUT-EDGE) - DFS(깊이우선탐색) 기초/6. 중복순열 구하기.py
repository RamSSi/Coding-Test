import sys


def DFS(L):
    global cnt
    if L == M:
        cnt += 1
        for e in res:
            print(e, end=" ")
        print()
        return
    for i in range(1, N+1):
        res[L] = i
        DFS(L+1)


if __name__ == "__main__":
    N, M = map(int, input().split())
    cnt = 0
    res = [0] * M
    DFS(0)
    print(cnt)
