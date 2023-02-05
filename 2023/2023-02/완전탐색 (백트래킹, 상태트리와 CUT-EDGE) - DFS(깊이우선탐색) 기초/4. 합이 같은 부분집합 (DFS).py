import sys

input = sys.stdin.readline


# def DFS(v):
#     if v == n:
#         s1 = 0
#         s2 = 0
#         for i in range(n):
#             if ch[i] == 0:
#                 s1 += ch[i]
#             else:
#                 s2 += ch[i]
#         if s1 == s2:
#             print(s1, s2, ch)
#             print("YES")
#             sys.exit(0)

#     else:
#         ch[v] = 1
#         DFS(v+1)
#         ch[v] = 0
#         DFS(v+1)


# if __name__ == "__main__":
#     n = int(input().strip())
#     a = list(map(int, input().split()))
#     ch = [0] * n
#     DFS(n)
#     print("NO")

def DFS(L, sum):
    if sum > total // 2:
        return
    if L == n:
        if sum == (total - sum):
            print("YES")
            sys.exit(0)
    else:
        DFS(L+1, sum+a[L])
        DFS(L+1, sum)


if __name__ == "__main__":
    n = int(input().strip())
    a = list(map(int, input().split()))
    total = sum(a)
    DFS(0, 0)
    print("NO")
