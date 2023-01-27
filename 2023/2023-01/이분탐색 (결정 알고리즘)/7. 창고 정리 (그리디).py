import sys

input = sys.stdin.readline

L = int(input())
boxes = list(map(int, input().split()))
M = int(input())
boxes.sort()

for i in range(M):
    boxes[-1] -= 1
    boxes[0] += 1
    boxes.sort()

print(boxes[-1]-boxes[0])
