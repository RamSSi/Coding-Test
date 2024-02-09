# 02493 탑

# 시간 초과 (O(N^2))

import sys

n = int(input())
stack = []
ans = []
for _ in range(n):
    stack.append(int(sys.stdin.readline()))

while stack:
    a = stack.pop()
    l = len(stack)
    c = 0
    while stack and a > stack[c-1]:
        if l == -c:
            break
        c -= 1
    ans.append(l + c)

print(*ans, sep=" ")


# 사람들이 푼 코드 (O(N))
import sys

n=int(sys.stdin.readline())
stack=[]
arr=list(map(int,sys.stdin.readline().rstrip().split()))
for i in range(n):
    while stack and stack[-1][1]<arr[i]:
        stack.pop()
    if stack:
        print(stack[-1][0],end=' ')
    else :
        print("0",end=' ')
    stack.append((i+1,arr[i]))