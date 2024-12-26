arr = []

for _ in range(9):
    arr.append(list(map(int, input().split())))

num = 0
l = []
for r in range(9):
    for c in range(9):
        if arr[r][c] >= num:
            l = []
            num = arr[r][c]
            l.append(r + 1)
            l.append(c + 1)

print(num)
print(*l)