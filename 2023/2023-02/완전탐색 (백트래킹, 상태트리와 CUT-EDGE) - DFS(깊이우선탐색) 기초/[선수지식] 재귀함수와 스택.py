import sys
input = sys.stdin.readline


def DFS(x):
    # 1번 방법
    # if x < 1:
    #     return
    # print(x)
    # DFS(x-1)

    # 2번 방법
    if x > 0:
        print(x)
        DFS(x-1)


if __name__ == "__main__":
    n = int(input().strip())
    DFS(n)
