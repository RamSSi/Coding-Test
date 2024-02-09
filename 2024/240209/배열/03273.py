# 03273 두 수의 합
import sys
n = int(input())
a = list(map(int, sys.stdin.readline().split()))
x = int(input())
l, r = 0, n-1
ans = 0

a.sort()

while l < r:
    result = a[l] + a[r]
    if x == result:
        ans += 1
        l += 1
        r = n-1
    elif x > result:
        l += 1
    elif x < result:
        r -= 1
print(ans)


# 03273 두 수의 합
n = int(input())
nums = set(map(int, input().split()))
x = int(input())

ans = 0
for num in nums:
    if x - num in nums:
        ans += 1

print(ans // 2)

# Set (Hash Table로 되어 있고, 중복이 없음 -> 탐색 속도 짱 빠름)
# List (Array로 되어 있고, 중복 있음 -> 탐색 속도 최악의 경우 O(N))

# 이 문제는 데이터가 최대 백만 개라서 List 대신 Set으로 푸는게 좋은 문제였다.. 