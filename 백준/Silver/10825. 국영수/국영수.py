n = int(input())
stu = []

for _ in range(n):
    name, a, b, c = map(str, input().split())
    stu.append((name, int(a), int(b), int(c)))

for name, a, b, c in sorted(stu, key=lambda x:(-x[1], x[2], -x[3], x[0])):
    print(name)