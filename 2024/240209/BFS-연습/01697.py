# 01697 숨바꼭질

import sys
from collections import deque

n, k = map(int, input().split())
q = deque([(n, 0)])

v = [False] * 100001

def bfs(k, q):
    while q:
        (cn, count) = q.popleft()
        if cn == k:
            return count
            
        else:
            if 0 <= cn-1 <= 100000 and v[cn-1] == False:
                q.append((cn-1, count+1))
                v[cn-1] = True
            if 0 <= cn+1 <= 100000 and v[cn+1] == False:
                q.append((cn+1, count+1))
                v[cn+1] = True
            if 0 <= cn*2 <= 100000 and v[cn*2] == False:
                q.append((cn*2, count+1))
                v[cn*2] = True
    
print(bfs(k,q))