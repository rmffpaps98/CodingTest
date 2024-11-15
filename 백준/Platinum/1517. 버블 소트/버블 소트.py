import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def merge_sort_and_count(arr, temp, left, right):
    if left >= right:
        return 0

    mid = (left + right) // 2

    count = merge_sort_and_count(arr, temp, left, mid)
    count += merge_sort_and_count(arr, temp, mid + 1, right)

    count += merge_and_count(arr, temp, left, mid, right)

    return count


def merge_and_count(arr, temp, left, mid, right):
    i = left
    j = mid + 1
    k = left
    count = 0

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            i += 1
        else:
            temp[k] = arr[j]
            count += (mid - i + 1)
            j += 1
        k += 1

    while i <= mid:
        temp[k] = arr[i]
        i += 1
        k += 1

    while j <= right:
        temp[k] = arr[j]
        j += 1
        k += 1

    for i in range(left, right + 1):
        arr[i] = temp[i]

    return count


n = int(input())
nums = list(map(int, input().split()))

temp = [0] * n
swap_count = merge_sort_and_count(nums, temp, 0, n - 1)

print(swap_count)