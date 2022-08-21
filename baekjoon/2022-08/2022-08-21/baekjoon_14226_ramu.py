# 14226 : 이모티콘

import sys
input = sys.stdin.readline

N = int(input())
display = 1
clip = 0
sec = 0

while display != N:
    clip += display
    sec += 1
    display += clip
    sec += 1
    while display > N:
        display -= N
        sec -= 1

