n, k = map(int, input().split())
st = sorted(list(map(int, input().split())))

print(st[-k:][0])