import sys
input = sys.stdin.readline

n, c = map(int, input().split())

hub = sorted([int(input()) for _ in range(n)])
start, end = 1, hub[-1] - hub[0]
answer = 0

while start <= end:
    mid = (start + end) // 2
    cur = hub[0]
    cnt = 1
    for i in range(1, n):
        if hub[i] - cur >= mid:
            cnt += 1
            cur = hub[i]

    if cnt >= c:
        if answer < mid:
            answer = mid
        start = mid + 1
    else:
        end = mid - 1

print(answer)