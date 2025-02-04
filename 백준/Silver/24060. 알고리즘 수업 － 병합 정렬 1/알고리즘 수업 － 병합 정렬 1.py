def merge_sort(arr, p, r, k):
    if p < r:
        q = (p + r) // 2
        left_res = merge_sort(arr, p, q, k)
        if left_res is not None:
            return left_res

        right_res = merge_sort(arr, q + 1, r, k)
        if right_res is not None:
            return right_res

        return merge(arr, p, q, r, k)
    return None


def merge(arr, p, q, r, k):
    global cnt
    i = p
    j = q + 1
    tmp = []

    while i <= q and j <= r:
        if arr[i] <= arr[j]:
            tmp.append(arr[i])
            i += 1
        else:
            tmp.append(arr[j])
            j += 1

    while i <= q:
        tmp.append(arr[i])
        i += 1

    while j <= r:
        tmp.append(arr[j])
        j += 1

    i = p
    t = 0

    while i <= r:
        arr[i] = tmp[t]
        cnt += 1
        if cnt == k:
            return arr[i]
        i += 1
        t += 1

    return None


a, k = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0

result = merge_sort(arr, 0, a - 1, k)
print(result if result is not None else -1)