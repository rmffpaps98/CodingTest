n, k = map(int, input().split())

if n == 0:
    print(1)
else:
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    dp[0][0] = 1

    for j in range(1, k + 1):
        for i in range(n + 1):
            dp[i][j] = dp[i][j - 1]
            if i > 0:
                dp[i][j] += dp[i - 1][j]

    print(dp[n][k] % 1000000000)