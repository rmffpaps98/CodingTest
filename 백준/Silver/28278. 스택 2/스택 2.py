import sys
input = sys.stdin.readline

n = int(input())
arr = []

for _ in range(n):
    ip = list(map(int, input().split()))

    if ip[0] == 1:
        arr.append(ip[1])
    elif ip[0] == 2:
        if not arr:
            print(-1)
        else:
            print(arr.pop())
    elif ip[0] == 3:
        print(len(arr))
    elif ip[0] == 4:
        if arr:
            print(0)
        else:
            print(1)
    else:
        if arr:
            print(arr[-1])
        else:
            print(-1)