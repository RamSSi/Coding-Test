import sys

input = sys.stdin.readline

n = int(input().strip())

def hanoi(num, start, dest):
    if num > 1:
        hanoi(num-1, start, 6 - start - dest)

    print(f'원반 {num} : {start} -> {dest}')

    if num > 1:
        hanoi(num-1, 6 - start - dest, dest)

hanoi(n, 1, 3)