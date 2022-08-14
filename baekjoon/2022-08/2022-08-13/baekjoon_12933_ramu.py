<<<<<<< HEAD
# 12933 : 오리

import sys
inputDuck = list(input())
ducklist = []
num = 0
end = False

cry = ['q', 'u', 'a', 'c', 'k']

for ch in inputDuck:
    if ch == 'q':   # q일 때
        if num == 0:    # 오리가 0마리이면
            ducklist.append([ch])   # 추가
            print(0)
            num += 1
        else:   # 오리가 1마리 이상이면
            print(1)
            for i in range(num):    # 오리들 다 검사
                if ducklist[i][-1] == 'k':  # 다 운 오리가 있으면 
                    ducklist[i].append(ch)  # 추가
                    print('1-1')
                    break
                elif i == (num - 1):  # 마지막 오리도 다 울지 않았다면 끝!
                    end = True
                    print('1-2')
=======
import sys

cry = {'q': 0, 'u': 1, 'a': 2, 'c': 3, 'k': 4}

crying = list(input())
ducks = []
num = 0
end = False

for ch in crying:
    if ch == 'q':
        # 처음 시작
        if num == 0:
            ducks.append([ch])
            num += 1
        # 오리가 있으면
        else:
            for i in range(num):
                if ducks[i][-1] == 'k':
                    ducks[i].append(ch)
                    break
                if i == num - 1:
                    ducks.append([ch])
                    num += 1
>>>>>>> bd14668e9b5ad983e0b211eeb46e77d4fa9753b2
                    break
    else:
        if num == 0:
            end = True
            break
<<<<<<< HEAD
        idx = cry.index(ch)
        for i in range(len(ducklist)):
            if ducklist[i][-1] == cry[idx-1]:
                ducklist[i].append(ch)
                break
            elif i == (num-1):
                end = True
                break
    if end == True:
        break

if end == True:
    print(-1)
else:
    print(num)      
        
=======
        else:
            for i in range(num):
                if cry[ch] == cry[ducks[i][-1]] + 1:
                    ducks[i].append(ch)
                    break
                if i == num - 1:
                    end = True
                    break
for duck in ducks:
    if duck[-1] != 'k':
        end = True
        break

if end:
    print(-1)
else:
    print(num)
>>>>>>> bd14668e9b5ad983e0b211eeb46e77d4fa9753b2
