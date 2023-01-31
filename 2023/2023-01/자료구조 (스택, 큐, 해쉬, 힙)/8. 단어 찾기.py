import sys

input = sys.stdin.readline

N = int(input().strip())
w = dict()

for i in range(N):
    word = input().strip()
    w[word] = 1

for i in range(N-1):
    word = input().strip()
    w[word] = 0

for key, val in w.items():
    if val == 1:
        print(key)
        break
