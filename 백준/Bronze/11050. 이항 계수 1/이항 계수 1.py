def f(n):
    if n <= 1:
        return 1
    return n * f(n-1)


n, k = map(int, input().split())
print(f(n) // (f(n-k) * f(k)))