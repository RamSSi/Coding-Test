# 15486 : 퇴사 2
import sys

input = sys.stdin.readline

N = int(input())

counseling = []

for i in range(N):
    (a, b) = map(int, input().split())
    counseling.append((i+1, a, b, b/a))

bigProfit = sorted(counseling, key=lambda x: x[3], reverse=True)

result = 0

schedule = [0] * N
confirm = [0] * N
possible = True

for (idx, days, pay, profit) in bigProfit:
    if idx + days > N:
        continue
    for i in range(idx, days):
        if schedule[i] != 0:
            possible = False
    if possible == True:
        confirm[idx] = True
        for i in range(idx, idx+days):
            schedule[i] = 1
for i in range(N):
    if confirm[i] == True:
        result += counseling[i-1][2]
print(result)