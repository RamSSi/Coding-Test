from typing import MutableSequence


def q_sort(a: MutableSequence, left: int, right: int) -> None:
    pl = left
    pr = right

    x = a[(left + right) // 2]

    print(f'a[{left}] ~ a[{right}] : ', *a[left:right+1])

    while pl <= pr:
        while a[pl] < x:
            pl += 1
        while a[pr] > x:
            pr -= 1
        if pl <= pr:
            a[pl], a[pr] = a[pr], a[pl]
            pl += 1
            pr -= 1

    if left < pr:
        q_sort(a, left, pr)
    if pl < right:
        q_sort(a, pl, right)


a = [4, 5, 2,  7, 6, 5, 1, 3]
q_sort(a, 0, 7)
