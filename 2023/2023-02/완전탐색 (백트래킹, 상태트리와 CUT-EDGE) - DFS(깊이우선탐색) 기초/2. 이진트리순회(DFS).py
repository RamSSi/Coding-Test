import sys


def DFS(v):
    if v > 7:
        return
    else:
        DFS(2*v)
        DFS(2*v+1)
        print(v, end=" ")   # 후위 순회


if __name__ == "__main__":
    DFS(1)
