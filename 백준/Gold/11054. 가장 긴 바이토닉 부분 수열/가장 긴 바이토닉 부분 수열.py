a = int(input())
nums = list(map(int, input().split()))

if a == 0:
    print(0)
else:
    inc_dp = [1] * a
    dec_dp = [1] * a

    for i in range(1, a):
        for j in range(i):
            if nums[i] > nums[j]:
                inc_dp[i] = max(inc_dp[i], inc_dp[j] + 1)

    for i in range(a - 2, -1, -1):
        for j in range(a - 1, i, -1):
            if nums[i] > nums[j]:
                dec_dp[i] = max(dec_dp[i], dec_dp[j] + 1)

    max_len = 0
    for i in range(a):
        max_len = max(max_len, inc_dp[i] + dec_dp[i] - 1)

    print(max_len)