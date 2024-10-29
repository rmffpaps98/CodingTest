a = int(input())

if a == 0:
    print(0)
else:
    nums = list(map(int, input().split()))

    dp = [0] * a
    dp[0] = nums[0]

    for i in range(1, a):
        dp[i] = nums[i]
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + nums[i])

    print(max(dp))