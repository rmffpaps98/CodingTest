n, m = map(int, input().split())
a = set(map(int, input().split()))
b = set(map(int, input().split()))

ab = a.difference(b)
ba = b.difference(a)

print(len(ab.union(ba)))