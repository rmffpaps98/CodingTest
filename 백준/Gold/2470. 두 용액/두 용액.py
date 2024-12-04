import sys
input = sys.stdin.readline

n = int(input())
sol = list(map(int, input().split()))


def two_sum(arr):
    arr.sort()
    left, right = 0, len(arr)-1
    min_sum = float('inf')
    result = (arr[left], arr[right])

    while left < right:
        current_sum = arr[left] + arr[right]

        if abs(current_sum) < abs(min_sum):
            min_sum = current_sum
            result = (arr[left], arr[right])

        if current_sum < 0:
            left += 1
        elif current_sum > 0:
            right -= 1
        else:
            break

    return result


print(*two_sum(sol))