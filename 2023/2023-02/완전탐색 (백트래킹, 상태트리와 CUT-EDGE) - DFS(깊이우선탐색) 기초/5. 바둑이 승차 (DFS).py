from itertools import combinations
import sys

input = sys.stdin.readline


def DFS(L, sum, tsum):
    global res
    # 남은 바둑이들을 모두 더해도 최대 무게보다 작으면 판단 안해도 된다!
    if sum + (total-tsum) < res:
        return
    if sum > C:
        return
    if L == N:
        if sum > res:
            res = sum
        return
    DFS(L+1, sum+a[L], tsum+a[L])
    DFS(L+1, sum, tsum+a[L])


if __name__ == "__main__":
    C, N = map(int, input().split())
    a = [0] * N

    for i in range(N):
        a[i] = int(input().strip())
    total = sum(a)
    res = 0
    DFS(0, 0, 0)
    print(res)
