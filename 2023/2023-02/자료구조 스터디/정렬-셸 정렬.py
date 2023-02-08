from typing import MutableSequence


def shell_sort(a: MutableSequence) -> None:
    n = len(a)
    k = n // 2
    while k > 0:
        for i in range(k, n):
            j = i - k
            tmp = a[i]
            while j >= 0 and a[j] > tmp:
                a[j+k] = a[j]
                j -= k
            a[j+k] = tmp
        k //= 2


if __name__ == "__main__":
    a = [8, 1, 4, 2, 7, 6, 3, 5]

    print(a)
    shell_sort(a)
    print(a)
