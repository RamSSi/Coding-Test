from typing import MutableSequence


def selection_sort(a: MutableSequence) -> None:
    n = len(a)
    for i in range(n-1):
        min = i
        for j in range(i+1, n):
            if a[j] < a[min]:
                min = j
        a[i], a[min] = a[min], a[i]


if __name__ == "__main__":
    a = [6, 4, 3, 7, 1, 9, 8]

    print("원래 배열 : ", a)
    selection_sort(a)
    print("정렬된 배열 : ", a)
