import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
b = deque(enumerate(map(int, input().split())))
result = []

while b:
    idx, num = b.popleft()
    result.append(idx+1)

    if num > 0:
        b.rotate(-(num - 1))
    else:
        b.rotate(-num)

print(' '.join(map(str, result)))