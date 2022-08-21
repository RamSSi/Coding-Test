# 배열 인덱스 이용
# 만약 누군가의 배수가 아니면 cnt += 1
# 이후 이 수의 배수 index들의 값을 1 해줌 (소수가 아니다!)

import sys
N = int(input())
ch = [0] * (N + 1) # 체 역할을 하는 list : 소수가 아니면 값이 1
cnt = 0
for i in range(2, N + 1):
    if ch[i] == 0:
        cnt += 1
        for j in range(i, N + 1, i):
            ch[j] = 1

print(cnt)