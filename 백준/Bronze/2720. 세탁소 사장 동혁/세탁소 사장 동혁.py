n = int(input())
coin = [25, 10, 5, 1]
money = [int(input()) for _ in range(n)]

for i in money :
    change = []
    for j in coin :
        change.append(i//j)
        i %= j
    print(*change)