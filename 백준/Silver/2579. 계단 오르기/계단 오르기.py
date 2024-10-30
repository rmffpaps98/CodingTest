n = int(input())
scores = [int(input()) for _ in range(n)]

if len(scores) <= 2:
    print(sum(scores))
else:
    dp = [0] * n
    dp[0] = scores[0]
    dp[1] = scores[0] + scores[1]

    for i in range(2, n):
        dp[i] = max(dp[i - 2] + scores[i], dp[i - 3] + scores[i - 1] + scores[i])

    print(dp[-1])