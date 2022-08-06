import sys
N = int(input())

students = list(list(map(int, sys.stdin.readline().split())) for _ in range(N * N))

classroom = [[0] * N for _ in range(N)]

dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def condition1(like):
    maxf = 0
    best = []
    for i in range(N):
        for j in range(N):
            cnt = 0
            for (dr, dc) in dir:
                nr, nc = i + dr, j + dc
                if 0 <= nr < N and 0 <= nc < N and classroom[nr][nc] != 0:
                    for friend in like:
                        if classroom[nr][nc] == friend:
                            cnt += 1
            if (i, j) not in fixed:
                if cnt > maxf:
                    maxf = cnt
                    best = [(i, j)]
                elif cnt == maxf:
                    best.append((i, j))
                if cnt == 4:
                    return [(i, j)]
    return best

def condition2(betters):
    maxSpace = 0
    best = []
    for better in betters:
        i, j = better
        if classroom[i][j] != 0:
            continue
        cnt = 0
        for (dr, dc) in dir:
            nr, nc = i + dr, j + dc
            if 0 <= nr < N and 0 <= nc < N and classroom[nr][nc] == 0:
                cnt += 1
        if (i, j) not in fixed:        
            if cnt > maxSpace:
                maxSpace = cnt
                best = [(i, j)]
            elif cnt == maxSpace:
                best.append((i, j))   
            if cnt == 4:
                return [(i, j)]
    if len(best) == 0:        
        for i in range(N):
            for j in range(N):
                if (i, j) not in fixed:
                    best = [(i, j)]
    return best

fixed = []
for studentInfo in students:
    student = studentInfo[0]
    like = studentInfo[1:]
    best1 = condition1(like)
    if len(best1) == 1:
        print(student, "조건1", best1) 
        (r, c) = best1[0]
        classroom[r][c] = student
        fixed.append((r, c))
        print(classroom)
    else:
        best2 = condition2(best1)
        print(student, "조건2", best2)
        (r, c) = best2[0]
        classroom[r][c] = student
        fixed.append((r, c))
        print(classroom)
    print("fixed:", fixed)

print(classroom)