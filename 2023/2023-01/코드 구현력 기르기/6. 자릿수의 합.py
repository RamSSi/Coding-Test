import sys

input = sys.stdin.readline

N = int(input())
nList = list(input().split())

# def digit_sum(num):
#     numToChar = list(num)
#     sumValue = 0
#     for i in numToChar:
#         sumValue += int(i)
#     return sumValue

# maxValue = (0, 0)
# for num in nList:
#     sumValue = digit_sum(num)
#     if maxValue[1] < sumValue:
#         maxValue = (num, sumValue)

# print(maxValue[0])


def digit_sum(num):
    sum = 0
    while num > 0:
        sum += num % 10
        num //= 10
    return sum


maxSum = 0
result = 0
for num in nList:
    currSum = digit_sum(int(num))
    if currSum > maxSum:
        maxSum = currSum
        result = int(num)

print(result)
