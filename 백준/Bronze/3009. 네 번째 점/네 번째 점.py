arr1 = []
arr2 = []

for _ in range(3):
    a, b = map(int, input().split())
    arr1.append(a)
    arr2.append(b)

print(*[i for i in arr1 if arr1.count(i) == 1], end=" ")
print(*[i for i in arr2 if arr2.count(i) == 1])