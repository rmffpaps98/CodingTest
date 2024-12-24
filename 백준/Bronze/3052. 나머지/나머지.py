arr = set()

for _ in range(10):
    num = int(input())
    arr.add(num%42)

print(len(arr))