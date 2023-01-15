import sys

input = sys.stdin.readline

N = int(input())
nList = list(map(int, input().split()))

avg = int(sum(nList)/N + 0.5)
answerLi = []
answer = 0
minGap = 100
maxNum = 0

answer = 0

for i in range(N):
    if abs(avg - nList[i]) < minGap:
        minGap = abs(avg - nList[i])
        answer = i
    elif abs(avg - nList[i]) == minGap:
        if nList[answer] < nList[i]:
            answer = i


# 반올림 방법
# python은 round() 함수를 사용하면 round_half_even 방식을 택한다.
# 소수 첫째 자리 반올림 시 0.5에서는 가까운 짝수를 찾는다.
# 예. round(67.5) => 68
#     round(66.5) => 66
# 따라서 0.5를 더한 후 int로 형변환하는 방식으로 반올림 한다.
print(avg, answer+1)
print(int(67.4+0.5))
print(int(67.5+0.5))
print(int(67.6+0.5))
print(round(67.4))
print(round(67.5))
print(round(67.6))
print(round(66.4))
print(round(66.5))
print(round(66.6))
