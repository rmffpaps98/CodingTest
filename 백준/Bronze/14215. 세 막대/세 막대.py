bar = sorted(list(map(int, input().split())))
if bar[0] + bar[1] > bar[2]:
    print(sum(bar))
else:
    print((bar[0] + bar[1]) * 2 - 1)