n = int(input())

wine = [0] + [int(input()) for _ in range(n)]

dp = [0] * (n + 1)

if n == 1:
    print(wine[1])
elif n == 2:
    print(wine[1] + wine[2])
else:
    dp[1] = wine[1]
    dp[2] = wine[1] + wine[2]

    for i in range(3, n + 1):
        dp[i] = max(dp[i - 1], wine[i] + wine[i - 1] + dp[i - 3], wine[i] + dp[i - 2])

    print(max(dp))