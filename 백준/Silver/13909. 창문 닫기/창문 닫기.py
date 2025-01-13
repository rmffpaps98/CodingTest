n = int(input())

sqrt_n = 0
while (sqrt_n + 1) * (sqrt_n + 1) <= n:
    sqrt_n += 1

print(sqrt_n)