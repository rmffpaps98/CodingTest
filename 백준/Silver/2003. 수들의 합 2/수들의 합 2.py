import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))


def target_sum_subarray(arr, m):
    left, right = 0, 1
    cnt = 0

    while right <= n and left <= right:
        current = sum(arr[left:right])

        if current == m:
            cnt += 1
            right += 1
        elif current < m:
            right += 1
        else:
            left += 1

    return cnt


print(target_sum_subarray(a, m))