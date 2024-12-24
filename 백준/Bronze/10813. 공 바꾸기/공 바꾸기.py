import sys
input = sys.stdin.readline

n, m = map(int, input().split())
basket = {i : i for i in range(1, n+1)}
for _ in range(m):
    i, j = map(int, input().split())
    basket[i], basket[j] = basket[j], basket[i]

print(*basket.values())