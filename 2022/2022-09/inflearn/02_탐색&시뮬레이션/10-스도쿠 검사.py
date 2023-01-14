import sys

input = sys.stdin.readline


sdo = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]
succ = True

def nine():
    succ = True
    for i in range(9):
        n = [0] * 10
        if succ == True:
            for j in range(9):
                if n[sdo[i][j]] == 1:
                    succ = False
                    break
                else:
                    n[sdo[i][j]] = 1
    return succ

def three():
    succ = True
    x = y = 0
    while succ == True and x <= 7:
        n = [0]*10
        for i in range(3):
            if succ == True:
                for j in range(3):
                    space = sdo[x+i][y+j]
                    if n[space] == 1:
                        succ = False
                        break 
                    else:
                        n[space] = 1
        if y <= 3:
            y+= 3
        else:
            y = 0
            x += 3
    return succ

if nine() and three():
    print("YES")
else:
    print("NO")