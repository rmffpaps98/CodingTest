import sys
input = sys.stdin.readline

n, m = map(int, input().split())
cards = list(map(int, input().split()))

for i in range(m) :
    cards.sort()
    x = cards.pop(0)
    y = cards.pop(0)
    num = x + y
    cards.append(num)
    cards.append(num)

print(sum(cards))