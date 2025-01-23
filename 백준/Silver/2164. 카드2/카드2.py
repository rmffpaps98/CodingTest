from collections import deque

n = int(input())
num = deque(range(1, n+1))

while True:
    if len(num) > 1:
        num.popleft()
    else:
        break

    if len(num) > 1:
        num.append(num.popleft())
    else:
        break

print(*num)