import sys

input = sys.stdin.readline

K, N = map(int, input().split())
loop = list(int(input()) for _ in range(K)) 
print(loop)

loop.sort()

l = 1
r = loop[-1]
cnt = 0

length = 0
while l <= r:
	cnt = 0
	mid = (l + r) // 2
	for i in loop:
		cnt += (i // mid)
		if cnt >= N:
			length = mid
			l = mid + 1
		else:
			r = mid - 1
	print(mid, length, cnt)
print(length)