import sys
input = sys.stdin.readline

n = int(input())
p = list(map(int, input().split()))

p.sort()

t = 0
for idx, time in enumerate(p):
    t += time * (n - idx)

print(t)