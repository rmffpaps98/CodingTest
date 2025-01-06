n, m = map(int, input().split())
cards = list(map(int, input().split()))
bj = 0

for i in range(len(cards) - 2):
    for j in range(i + 1, len(cards) - 1):
        for k in range(j + 1, len(cards)):
            current_sum = cards[i] + cards[j] + cards[k]
            if current_sum == m:
                bj = m
                break
            if current_sum < m:
                bj = max(bj, current_sum)

print(bj)