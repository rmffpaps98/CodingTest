def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


a, b = map(int, input().split())
c, d = map(int, input().split())

num = (a * d) + (b * c)
den = (b * d)

g = gcd(num, den)

print(num // g, den // g)