import sys

input = sys.stdin.readline

card = [i for i in range(21)]

for i in range(10):
    a, b = map(int, input().split())
    card[a:b+1] = card[b:a-1:-1]

print(card[1:])

# 5 10
# 9 13
# 1 2
# 3 4
# 5 6
# 1 2
# 3 4
# 5 6
# 1 20
# 1 20
