n = int(input())
mem = []

for _ in range(n):
    age, name = map(str, input().split())
    mem.append((int(age), name))

for age, name in sorted(mem, key=lambda x: x[0]):
    print(age, name)