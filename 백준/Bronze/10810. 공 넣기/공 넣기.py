import sys
input = sys.stdin.readline

n, m = map(int, input().split())
basket = {i : 0 for i in range(1, n+1)}
for _ in range(m):
    i, j, k = map(int, input().split())
    for num in range(i, j+1):
        basket[num] = k

print(*basket.values())