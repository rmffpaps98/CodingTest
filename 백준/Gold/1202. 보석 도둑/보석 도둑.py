import sys, heapq

input = sys.stdin.readline

n, k = map(int, input().split())

jewel = [list(map(int, input().split())) for _ in range(n)]
max_weight = [int(input()) for _ in range(k)]
result = 0
tmp = []

jewel.sort()
max_weight.sort()

for i in max_weight :
    while jewel and jewel[0][0] <= i :
        heapq.heappush(tmp, -jewel[0][1])
        heapq.heappop(jewel)
    if tmp :
        result -= heapq.heappop(tmp)

print(result)