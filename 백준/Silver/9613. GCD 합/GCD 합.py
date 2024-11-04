def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

t = int(input())

for _ in range(t):
    answer = 0
    nums = list(map(int, input().split()))
    n = nums[0]
    nums = nums[1:]

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            answer += gcd(nums[i], nums[j])

    print(answer)