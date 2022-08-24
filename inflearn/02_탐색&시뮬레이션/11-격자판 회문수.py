import sys

input = sys.stdin.readline

nlist = [list(map(int, input().split())) for _ in range(7)]

cnt = 0

def row(i, j):
    st = [nlist[i][j]]
    for x in range(1, 5):
        if j+x >= 7:
            return False
        st.append(nlist[i][j+x])
    if st == st[::-1]:
        return True
    else:
        return False

def col(i, j):
    st = [nlist[i][j]]
    for x in range(1, 5):
        if i+x >= 7:
            return False
        st.append(nlist[i+x][j])
    if st == st[::-1]:
        return True
    else:
        return False
    

for i in range(7):
    for j in range(7):
        if row(i, j):
            cnt += 1
        if col(i, j):
            cnt += 1

print(cnt)