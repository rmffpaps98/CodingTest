import sys
input = sys.stdin.readline

# 1. Dictionary 활용
n = int(input())
cards = list(map(int, input().split()))
m = int(input())
nums = list(map(int, input().split()))

card_count = {}
for card in cards:
    if card in card_count:
        card_count[card] += 1
    else:
        card_count[card] = 1

result = []
for num in nums:
    result.append(card_count.get(num, 0))

print(*result)