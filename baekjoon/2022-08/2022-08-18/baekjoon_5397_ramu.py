# 5397 : 키로거

import sys

n = int(input())

for i in range(n):
    key = list(sys.stdin.readline().strip())
    left, right = [], []

    for ch in key:
        if ch == '<':
            if left:
                right.append(left.pop())
        elif ch == '>':
            if right:
                left.append(right.pop())
        elif ch == '-':
            if left:
                left.pop()
        else:
            left.append(ch)
    
    left.extend(reversed(right))
    
    print(''.join(left))