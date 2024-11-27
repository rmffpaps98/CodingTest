import sys
input = sys.stdin.readline

n = int(input())
nums = [int(input()) for i in range(n)]

#버블 정렬
# for i in range(n):
#     for j in range(n - i - 1):
#         if nums[j] > nums[j+1]:
#             nums[j], nums[j+1] = nums[j+1], nums[j]

#병합 정렬
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


print(*merge_sort(nums), sep='\n')