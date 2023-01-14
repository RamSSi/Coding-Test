# 삼성 SW Expert Academy - 2072 홀수만 더하기
import sys
input = sys.stdin.readline

result = []
for i in range(int(input())):
    sum = 0
    for n in list(map(int, input().split())):
        if n % 2 == 1:
            sum += n
    print('#' + str(i+1), sum)

