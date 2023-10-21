import sys
input = sys.stdin.readline

n, k = map(int, input().split())

device = list(map(int, input().split()))
plug = []
cnt = 0

for i in range(k):
    if device[i] in plug:
        continue

    if len(plug) < n :
        plug.append(device[i])
        continue

    priority = []
    for c in plug:
        if c in device[i:]:
            priority.append(device[i:].index(c))
        else:
            priority.append(101)
    target = priority.index(max(priority))
    plug.remove(plug[target])
    plug.append(device[i])
    cnt += 1

print(cnt)