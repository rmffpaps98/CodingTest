a = int(input())

nums = list(map(int, input().split()))

if a == 0:
    print(0)
else :
    dp = [1] * a
    for i in range(1, a):
        for j in range(i):
            if nums[j] > nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    print(max(dp))