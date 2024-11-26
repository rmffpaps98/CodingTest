import sys
input = sys.stdin.readline

n = int(input())
num1 = sorted(list(map(int, input().split())))

m = int(input())
num2 = list(map(int, input().split()))

def bs(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return 0

for i in num2:
    print(bs(num1, i))