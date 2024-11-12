import sys
input = sys.stdin.readline

n = int(input())
cards = list(map(int, input().split()))
m = int(input())
nums = {i: 0 for i in list(map(int, input().split()))}

for i in cards:
    if i in nums:
        nums[i] = nums.get(i) + 1

print(*(nums.values()))