# 01475 방 번호

import sys, math

ans = 0
nums = [0] * 10
for n in sys.stdin.readline().strip():
  nums[int(n)] += 1

for i in range(10):
  if i != 6 and i != 9:
    if nums[i] > ans:
      ans = nums[i] 
a = math.ceil((nums[6] + nums[9]) / 2)
if ans < a:
  ans = a

print(ans)

# =======================================

a = [0] * 10
for n in input():
  a[int(n)] += 1
a[6] = (a[6] + a.pop(-1) + 1) // 2
print(max(a))