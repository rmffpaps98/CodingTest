n, m = map(int, input().split())

nn = set()
mm = set()

for _ in range(n):
    nn.add(input())

for _ in range(m):
    mm.add(input())

nm = nn.intersection(mm)
print(len(nm))

for i in sorted(nm):
    print(i)