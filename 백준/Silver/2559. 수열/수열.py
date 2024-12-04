import sys
input = sys.stdin.readline

n, k = map(int, input().split())
temperature = list(map(int, input().split()))


def max_sum_subarray(arr, k):
    if len(arr) < k:
        return None

    max_sum = current_sum = sum(arr[:k])

    for i in range(k, len(arr)):
        current_sum += arr[i] - arr[i-k]
        max_sum = max(max_sum, current_sum)

    return max_sum


print(max_sum_subarray(temperature, k))