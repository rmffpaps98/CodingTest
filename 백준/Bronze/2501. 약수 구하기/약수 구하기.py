p, q = map(int, input().split())
arr = []

for i in range(1, p+1):
    if p % i == 0:
        arr.append(i)

if len(arr) >= q:
    print(arr[q-1])
else:
    print(0)