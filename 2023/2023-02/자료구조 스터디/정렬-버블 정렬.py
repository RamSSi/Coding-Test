from typing import MutableSequence


def bubble_sort(a: MutableSequence) -> None:
    n = len(a)
    k = 0
    while k < n-1:
        last = n - 1
        for j in range(n-1, k, -1):
            if a[j-1] > a[j]:
                a[j-1], a[j] = a[j], a[j-1]
                last = j
        k = last


if __name__ == "__main__":
    a = [6, 4, 3, 7, 1, 9, 8]

    print("원래 배열 : ", a)
    bubble_sort(a)
    print("정렬된 배열 : ", a)
