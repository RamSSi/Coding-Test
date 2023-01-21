import sys

input = sys.stdin.readline
array = []
maxSum = 0

N = int(input())

for i in range(N):
    array.append(list(map(int, input().split())))

line1 = 0
line2 = 0
for a in range(N):
    rowSum = 0
    colSum = 0
    line1 += array[a][a]
    line2 += array[a][N-a-1]
    for b in range(N):
        rowSum += array[a][b]
        colSum += array[b][a]
    if maxSum < rowSum:
        maxSum = rowSum
    if maxSum < colSum:
        maxSum = colSum
if maxSum < line1:
    maxSum = line1
if maxSum < line2:
    maxSum = line2
print(maxSum)

# 5
# 10 13 10 12 15
# 12 39 30 23 11
# 11 25 50 53 15
# 19 27 29 37 27
# 19 13 30 13 19
