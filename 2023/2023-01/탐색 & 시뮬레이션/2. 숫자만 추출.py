import sys

input = sys.stdin.readline

s = input()

num = 0
cnt = 2
for i in s:
    # if 48 <= ord(i) <= 57:
    if i.isdecimal():
        num = num * 10 + int(i)
print(num)

for x in range(2, num//2+1):
    if num % x == 0:
        cnt += 1

print(cnt)

# g0en2Ts8eSoft
