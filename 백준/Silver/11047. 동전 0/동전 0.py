n, k = map(int, input().split())
coin = [int(input()) for _ in range(n)]
cnt = 0

for c in sorted(coin, reverse=True):
    if k >= c:
        cnt += k // c
        k %= c

print(cnt)