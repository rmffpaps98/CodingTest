n = int(input())
cnt = 0

for _ in range(n):
    w = input()
    prev = w[0]
    plist = []

    for i in w[1:]:
        if i not in plist:
            plist.append(prev)
            prev = i
        elif prev == i and i in plist:
            pass
        else:
            break
    else:
        cnt += 1

print(cnt)