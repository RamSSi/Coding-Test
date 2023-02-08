from typing import MutableSequence
import copy


def merge(a: MutableSequence, left: int, mid: int, right: int) -> None:
    L = copy.deepcopy(a[left:mid+1])
    R = copy.deepcopy(a[mid+1:right+1])

    i = j = 0
    k = left

    ll = len(L)
    rl = len(R)
    print(L, R)

    while i < ll and j < rl:
        if L[i] <= R[j]:
            a[k] = L[i]
            i += 1
        else:
            a[k] = R[j]
            j += 1
        k += 1

    while i < ll:
        a[k] = L[i]
        k += 1
        i += 1
    while j < rl:
        a[k] = R[j]
        k += 1
        j += 1


def merge_sort(a: MutableSequence, left: int, right: int) -> None:
    if left < right:
        center = (left + right)//2

        merge_sort(a, left, center)
        merge_sort(a, center+1, right)

        merge(a, left, center, right)


if __name__ == "__main__":
    a = [8, 1, 4, 2, 7, 6, 3, 5]

    print(a)
    merge_sort(a, 0, 7)
    print(a)
