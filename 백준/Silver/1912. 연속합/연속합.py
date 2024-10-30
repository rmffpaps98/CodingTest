a = int(input())
nums = list(map(int, input().split()))

if a == 0:
    print(0)
else:
    dp = [0] * a
    dp[0] = nums[0]

    for i in range(1, a):
        dp[i] = max(nums[i], dp[i-1] + nums[i])

    print(max(dp))