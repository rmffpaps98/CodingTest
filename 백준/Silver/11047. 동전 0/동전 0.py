import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = []

for _ in range(n):
    coins.append(int(input().strip()))

cnt = 0

while k > 0:
    coin = coins.pop()

    if k >= coin:
        count, rest = divmod(k, coin)
        cnt += count
        k = rest

print(cnt)