import sys
input = sys.stdin.readline


def hanoi(n, start, auxiliary, end):
    if n == 1:
        print(start, end)
        return

    hanoi(n - 1, start, end, auxiliary)
    print(start, end)
    hanoi(n - 1, auxiliary, start, end)


n = int(input())
print(2 ** n - 1)
hanoi(n, 1, 2, 3)