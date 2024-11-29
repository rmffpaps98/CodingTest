import sys
input = sys.stdin.readline

n = list(map(str, input().rstrip()))


def bubble(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr


print(''.join(bubble(n)))