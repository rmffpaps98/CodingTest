import sys
input = sys.stdin.readline

n = int(input())
p = set()
cnt = 0

for _ in range(n):
    a, b = input().split()
    if a in p or b in p:
        p.add(a)
        p.add(b)

    if a == 'ChongChong' or b == 'ChongChong':
        p.add(a)
        p.add(b)

print(len(p))