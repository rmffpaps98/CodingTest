import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
irons = list(map(int, input().split()))


def two_sum(arr, m):
    arr.sort()
    left, right = 0, len(arr)-1
    cnt = 0

    while left < right:
        current_sum = arr[left] + arr[right]

        if current_sum == m:
            cnt += 1
            left += 1
            right -= 1
        elif current_sum < m:
            left += 1
        else:
            right -= 1

    return cnt


print(two_sum(irons, m))