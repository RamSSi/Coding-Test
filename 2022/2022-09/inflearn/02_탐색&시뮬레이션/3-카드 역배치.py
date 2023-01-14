# import sys

# nlist = list(range(0, 21))
# for i in range(10):
#     a, b = map(int, input().split())
#     li = nlist[a:b+1]
#     newli = list(reversed(li))
#     n = 0
#     for j in range(a, b+1):
#         nlist[j] = newli[n]
#         n += 1
#     print(nlist)
# print(nlist[1:])

nlist = list(range(0, 21))

for i in range(10):
    a, b = map(int, input().split())
    for j in range((b-a+1)//2):
        nlist[a+j], nlist[b-j] = nlist[b-j], nlist[a+j]
    print(a, b, nlist)

print(*nlist[1:], sep=' ')