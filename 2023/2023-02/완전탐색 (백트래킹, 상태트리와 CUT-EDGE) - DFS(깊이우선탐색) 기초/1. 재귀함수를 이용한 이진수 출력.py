import sys

input = sys.stdin.readline


def binary(x):
    if x // 2 > 1:
        binary(x // 2)
    else:
        print(x // 2, end="")
    print(x % 2, end="")


def DFS(x):
    if x == 0:
        return
    else:
        DFS(x//2)
        print(x % 2, end="")


if __name__ == "__main__":
    N = int(input().strip())
    binary(N)
    DFS(N)
