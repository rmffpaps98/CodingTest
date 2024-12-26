k, q, l, b, n, p = map(int, input().split())

if k == 1:
    print(0, end=" ")
else:
    print(1-k, end=" ")

if q == 1:
    print(0, end=" ")
else:
    print(1-q, end=" ")

if l == 2:
    print(0, end=" ")
else:
    print(2-l, end=" ")

if b == 2:
    print(0, end=" ")
else:
    print(2-b, end=" ")

if n == 2:
    print(0, end=" ")
else:
    print(2-n, end=" ")

if p == 8:
    print(0)
else:
    print(8-p)