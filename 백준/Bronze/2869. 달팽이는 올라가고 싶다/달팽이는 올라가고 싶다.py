a, b, v = map(int, input().split())

r = v - a
d = a - b
days = 1 + (r + d - 1) // d
print(days)
