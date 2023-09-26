n = 1000 - int(input())
coins = [500, 100, 50, 10, 5, 1]
cnt = 0

for coin in coins:
    while n >= coin:
        n -= coin
        cnt += 1

print(cnt)