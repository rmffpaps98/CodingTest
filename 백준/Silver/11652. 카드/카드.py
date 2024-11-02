import sys

n = int(input())
cards = {}

for _ in range(n):
    i = int(sys.stdin.readline())
    cards[i] = cards.get(i, 0) + 1

for i in sorted(cards):
    if cards[i] == max(cards.values()):
        print(i)
        break