import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
lis = [a[0]]


def bs(target):
    start, end = 0, len(lis) - 1

    while start <= end:
        mid = (start + end) // 2
        if lis[mid] == target:
            return mid
        elif lis[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return start


for i in a:
    if lis[-1] < i:
        lis.append(i)
    else:
        idx = bs(i)
        lis[idx] = i

print(len(lis))