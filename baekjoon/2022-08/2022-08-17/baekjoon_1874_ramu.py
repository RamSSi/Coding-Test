# 1874 : 스택 수열

import sys
n = int(input())

stack = []
signs = []
result = []
curr = 0

for _ in range(n):
    num = int(sys.stdin.readline())
    if num > curr:
        stack += list(range(curr+1, num+1))
        signs += '+' * (num - curr)
        result.append(stack.pop())
        signs += '-'
        curr = num  

    elif num < curr:    # stack에 넣은 수가 num보다 클 경우
        p = stack.pop()
        if p == num:
            result.append(p)
            signs += '-'
        else:
            signs = 0
            break

if signs == 0:
    print("NO")
else:
    print(*signs, sep='\n')