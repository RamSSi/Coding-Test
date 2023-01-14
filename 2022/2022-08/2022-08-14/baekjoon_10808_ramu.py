# 10808 : 알파벳 개수

S = list(input())
al = [0] * (ord('z') - ord('a') + 1)

for ch in S:
    num = ord(ch) - ord('a')
    al[num] += 1

print(*al, sep=' ')