n = int(input())
nums = []

for _ in range(n):
    x, y = map(int, input().split())
    nums.append((x, y))

for x, y in sorted(nums, key=lambda x : (x[0], x[1])):
    print(x, y)