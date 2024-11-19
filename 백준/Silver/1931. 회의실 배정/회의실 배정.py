import sys
input = sys.stdin.readline

n = int(input().strip())
rooms = []
cnt = 0
t = 0

for _ in range(n):
    start, end = map(int, input().split())
    rooms.append((start, end))

rooms.sort(key=lambda x: (x[1], x[0]))

for s, e in rooms:
    if t <= s:
        cnt += 1
        t = e

print(cnt)