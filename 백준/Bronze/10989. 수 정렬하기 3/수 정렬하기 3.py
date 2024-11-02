import sys

n = int(input())
nums = {i: 0 for i in range(10001)}

for _ in range(n):
    nums[(int(sys.stdin.readline()))] += 1

for i in nums:
    if nums[i] != 0:
        for _ in range(nums[i]):
            print(i)