import sys
input = sys.stdin.readline

result = []
for i in range(int(input())):
    sum = 0
    for n in list(map(int, input().split())):
        if n % 2 == 1:
            sum += n
    result.append(('#'+ str(i+1), sum))

for (T, sum) in result:
    print(T, sum)
    
