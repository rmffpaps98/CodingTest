a, b = map(int, input().split())
c = int(input())

if c >= 60:
    a += (c//60)
    b += (c%60)
    if b - 60 >= 0:
        print((a+1)%24, b % 60)
    else:
        print(a % 24, b % 60)
else:
    b += c
    if b - 60 >= 0:
        print((a+1)%24, b % 60)
    else:
        print(a % 24, b % 60)