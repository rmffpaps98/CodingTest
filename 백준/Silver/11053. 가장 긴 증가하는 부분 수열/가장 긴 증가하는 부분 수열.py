a = int(input())

if a == 0:
    print(0)
else:
    nums = list(map(int, input().split()))

    dp = [1] * a

    for i in range(1, a):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    print(max(dp))