def f(n):
    if n <= 1:
        return 1
    return n * f(n - 1)


n = int(input())
for _ in range(n):
    n, m = map(int, input().split())
    print(f(m) // (f(m-n) * f(n)))