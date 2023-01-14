import sys

size = int(input())
a = list(map(int, sys.stdin.readline().split()))
a.sort()
N = int(input())
result1, result2 = 0, 0

for i in range(size):
    if a[i] == N:
        break
    elif a[i-1] < N < a[i]:
        result1 = N - a[i-1] - 1
        result2 = a[i] - N - 1
        break
    elif a[0] > N :
        result1 = N - 1
        result2 = a[0] - N - 1
        break

print(result1 * result2 + result1 + result2)
        

    

# idx = 0
# cnt = 0

# if N in a:
#     cnt = 0

# else:
#     if N < a[0]:
#         \
#         if N == a[0]-1:
#             cnt = N - 1
#         else:
            
#     else:
#         for i in range(1, size):
#             if a[i-1] < N < a[i]:
#                 if a[i-1]+1 == N:
#                     cnt = a[i] - 1 - N
#                 elif a[i+1] - 1 == N:
#                     cnt = N - (a[i] + 1)
#                 else:
#                     A = N - (a[i-1] + 1)
#                     B = a[i] - 1 - N
#                     cnt = (A * B) + A + B

# print(cnt)