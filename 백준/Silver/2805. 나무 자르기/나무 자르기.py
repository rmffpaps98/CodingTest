import sys
input = sys.stdin.readline

n, m = map(int, input().split())

trees = list(map(int, input().split()))
start, end = 1, max(trees)

while start <= end:
    mid = (start + end) // 2
    wood = 0
    for i in trees:
        if i >= mid:
            wood += i - mid

    if wood >= m:
        start = mid + 1
    else:
        end = mid - 1

print(end)