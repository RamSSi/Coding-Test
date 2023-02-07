# 8개의 퀸이 서로를 잡지 못하도록 8*8 체스판에 배치
# i: 열, j: 행
import sys

pos = [0] * 8
flag = [False] * 8
flag_a = [False] * 15
flag_b = [False] * 15

def put() -> None:
    # 각 열에 배치한 퀸의 위치를 출력
    for i in range(8):
        for j in range(8):
            print('■' if pos[i] == j else '□', end='')
        print()
    print()


def set(i: int) -> None:
    # i열에 퀸을 배치
    for j in range(8):
        if (    not flag[j]     # j행에 퀸이 없을 때
                and not flag_a[i+j]  # 대각선 방향으로 퀸이 없을 때
                and not flag_b[i-j+7]):  # 대각선 방향으로 퀸이 없을 때
            pos[i] = j  # 퀸을 j행에 배치
            if i == 7:
                put()  # 모든 열에 퀸 배치를 끝내고 출력
            else:
                flag[j] = flag_a[i+j] = flag_b[i-j+7] = True
                set(i + 1)  # 다음 열에 퀸 배치
                flag[j] = flag_a[i+j] = flag_b[i-j+7] = False


set(0)  # 0 열에 퀸을 배치 시작