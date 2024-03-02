import sys
input = sys.stdin.readline

dir = [(-1, 0), (0, -1), (1, 0), (0, 1)]

for _ in range(int(input())):

    result = "IMPOSSIBLE"
    cnt = 0
    
    # 맵 입력
    maps = []
    fire = []
    p = []
    m, n = map(int, input().split())
    
    for _ in range(n):
        maps.append(list(input().rstrip()))

    # 불과 상근 위치 확인
    for i in range(n):
        for j in range(m):
            if maps[i][j] == '*':
                fire.append((i, j))
            elif maps[i][j] == '@':
                p.append((i, j))

    while p:
        # 불 이동
        new_f = []
        for (fx, fy) in fire:
            for i in range(4):
                cx, cy = fx + dir[i][0], fy + dir[i][1]
                if 0 <= cx < n and 0 <= cy < m: 
                    if maps[cx][cy] != '#' and maps[cx][cy] != '*':
                        new_f.append((cx, cy))
                        maps[cx][cy] = '*'
        fire = new_f
        
        # 상근 이동
        new_p = []
            
        cnt += 1
        for (px, py) in p:
            for i in range(4):
                cx, cy = px + dir[i][0], py + dir[i][1]
                if 0 <= cx < n and 0 <= cy < m: 
                    if maps[cx][cy] == '.':
                        new_p.append((cx, cy))
                        maps[cx][cy] = 'p'
                # 탈출 성공
                else:
                    result = cnt
                    p = []
                    break
        if result != "IMPOSSIBLE":
            break    
        else: p = new_p
        
    print(result)