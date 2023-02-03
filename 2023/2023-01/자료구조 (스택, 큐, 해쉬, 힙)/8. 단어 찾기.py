import sys

input = sys.stdin.readline

N = int(input().strip())
word = dict()

for _ in range(N):
    word[input().strip()] = 0

for _ in range(N-1):
    word[input().strip()] = 1

for key, val in word.items():
    if val == 0:
        print(key)
        break
