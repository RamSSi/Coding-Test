# 10844 : 쉬운 계단 수

N = int(input())
result = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
N -= 1
while N > 0:
    curr = [0] * 10
    for i in range(10):
        if i == 0 and result[0] > 0:
            curr[1] += result[0]
        elif i == 9 and result[9] > 0:
            curr[8] += result[9]
        else:
            curr[i-1] += result[i]
            curr[i+1] += result[i]
    result = curr
    N -= 1            
cnt = 0
for i in result:
    cnt += i
print(cnt % 1000000000)
