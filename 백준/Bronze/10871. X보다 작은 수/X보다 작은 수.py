n, x = map(int, input().split())
arr = list(map(int, input().split()))
print(*[i for i in arr if i < x])