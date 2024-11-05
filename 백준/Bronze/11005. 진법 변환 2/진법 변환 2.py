n, b = map(int, input().split())

num = ''

while n > 0:
    n, mod = divmod(n, b)
    if mod < 10:
        num += str(mod)
    else:
        num += chr(55 + mod)

print(num[::-1])