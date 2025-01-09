import sys
input = sys.stdin.readline

n = int(input())
ent = set()

for _ in range(n):
    name, e = input().split()
    if e == 'enter':
        ent.add(name)
    else:
        ent.discard(name)

for name in sorted(ent, reverse=True):
    print(name)
