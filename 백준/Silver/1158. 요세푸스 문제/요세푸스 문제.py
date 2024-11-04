from collections import deque

n, k = map(int, input().split())
pp = deque(range(1, n+1))
answer = []

while pp:
    for _ in range(k-1):
        pp.append(pp.popleft())

    answer.append(str(pp.popleft()))

print('<' + ', '.join(answer) + '>')