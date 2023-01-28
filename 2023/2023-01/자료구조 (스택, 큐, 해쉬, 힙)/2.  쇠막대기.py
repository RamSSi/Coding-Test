import sys

input = sys.stdin.readline

arr = list(input().strip())

stack = []
res = 0

for i in range(len(arr)):
    if arr[i] == "(":
        stack.append(arr[i])
    else:
        stack.pop()
        if arr[i-1] == "(":
            res += len(stack)
        else:
            res += 1

# cnt = 0  # 현재 막대기 개수
# res = 0  # 전체 막대기 개수

# for i in range(len(arr)):
#     if arr[i] == ")":
#         cnt -= 1
#         if arr[i-1] == ")":
#             res += 1
#         else:
#             res += cnt
#         stack.pop()
#     else:
#         stack.append(arr[i])
#         cnt += 1

print(res)
