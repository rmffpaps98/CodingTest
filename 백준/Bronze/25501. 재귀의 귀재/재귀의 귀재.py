def rec(s, l, r, cnt):
    if l >= r:
        return 1, cnt
    elif s[l] != s[r]:
        return 0, cnt
    else:
        return rec(s, l+1, r-1, cnt+1)


n = int(input())

for _ in range(n):
    isp = input().strip()
    cnt = 1

    print(*rec(isp, 0, len(isp)-1, cnt))