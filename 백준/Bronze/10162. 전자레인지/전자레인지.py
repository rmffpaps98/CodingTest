T = int(input())
mw = [300, 60, 10]
btn = []

for i in mw:
    cnt = T // i
    T %= i
    btn.append(cnt)

if T > 0:
    print(-1)
else:
    print(*btn)