import heapq

N = int(input())
cards = []
for _ in range(N) :
    heapq.heappush(cards, int(input()))

S = 0

while len(cards) > 1 :
    n1 = heapq.heappop(cards)
    n2 = heapq.heappop(cards)
    S += n1 + n2
    heapq.heappush(cards, n1 + n2)

print(S)