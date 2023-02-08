from typing import MutableSequence


def insertion_sort(a: MutableSequence) -> None:
    n = len(a)
    for i in range(1, n):
        j = i
        tmp = a[i]
        while j > 0 and a[j-1] > tmp:
            a[j] = a[j-1]
            j -= 1
        a[j] = tmp


if __name__ == "__main__":
    a = [6, 4, 3, 7, 1, 9, 8]

    print("원래 배열 : ", a)
    insertion_sort(a)
    print("정렬된 배열 : ", a)
