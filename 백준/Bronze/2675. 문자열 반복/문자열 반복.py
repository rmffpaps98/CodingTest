t = int(input())

for _ in range(t):
    r, s = map(str, input().split())
    p = ''
    for i in s:
        p += i*int(r)
    print(p)