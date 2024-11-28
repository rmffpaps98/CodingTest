import sys
input = sys.stdin.readline

n = int(input())


def hanoi(n, start, via, end):
    if n == 1:
        print(start, end)
        return

    hanoi(n-1, start, end, via)
    print(start, end)
    hanoi(n-1, via, start, end)


print(2 ** n - 1)
hanoi(n, 1, 2, 3)