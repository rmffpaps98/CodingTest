from collections import deque

n, k = map(int, input().split())
yf = deque(range(1, n+1))
arr = []

while yf:
    for _ in range(k-1):
        yf.append(yf.popleft())

    arr.append(yf.popleft())

print('<', end='')
for i in arr:
    if i != arr[-1]:
        print(i, end=', ')
    else:
        print(i, end='')
print('>')