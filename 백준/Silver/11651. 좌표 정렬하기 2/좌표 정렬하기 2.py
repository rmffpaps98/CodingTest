n = int(input())
nums = []

for _ in range(n):
    x, y = map(int, input().split())
    nums.append((x, y))

for x, y in sorted(nums, key=lambda x: (x[1], x[0])):
    print(x, y)