import sys

input = sys.stdin.readline

N = int(input())

# maxReward = 0

# for order in range(N):
#     dice = [0] * 7
#     reward = 0
#     maxDice = 0
#     for num in list(map(int, input().split())):
#         dice[num] += 1
#     for i in range(1, 7):
#         if dice[i] == 3:
#             reward = 10000+i*1000
#             break
#         elif dice[i] == 2:
#             reward = 1000 + i * 100
#             break
#         elif dice[i] == 1:
#             maxDice = i
#     else:
#         reward = maxDice * 100
#     if reward > maxReward:
#         maxReward = reward
# print(maxReward)

res = 0
for i in range(N):
    tmp = list(map(int, input().split()))
    tmp.sort()
    a, b, c = tmp

    if a == b and b == c:
        money = 10000+a*1000
    elif a == b or a == c:
        money = 1000 + a*100
    elif b == c:
        money = 1000 + b * 100
    else:
        money = 100 * c
    if money > res:
        res = money
print(res)
