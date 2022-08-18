# 6198 : 옥상 정원 꾸미기

import sys
input = sys.stdin.readline

N = int(input())

buildings = list(int(sys.stdin.readline().strip()) for _ in range(N))

stack = []
cnt = 0
for b in buildings:
    while stack and stack[-1] <= b:
        stack.pop() # 왼쪽 건물 중 현재 건물을 볼 수 없는 건물은 빼기
    stack.append(b)
    cnt += len(stack) - 1

print(cnt)