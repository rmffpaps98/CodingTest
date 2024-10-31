t = int(input())

if t == 0:
    print(0)
else:
    dp = [0] * 101
    dp[1], dp[2], dp[3] = 1, 1, 1

    for _ in range(t):
        n = int(input())
        if dp[n] == 0:
            for i in range(4, n+1):
                dp[i] = dp[i-2] + dp[i-3]

        print(dp[n])