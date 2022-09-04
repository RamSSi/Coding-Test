import sys

input = sys.stdin.readline

stick = list(input().strip())
print(stick)
stack = []
cnt = 0
prev = '0'
for i in range (len(stick)):
    if stick[i] == '(':
        stack.append(stick[i])
    else:
        stack.pop()
        if stick[i-1] == '(':
            cnt += len(stack)
        else:
            cnt += 1

print(cnt)