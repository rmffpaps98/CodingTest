n = int(input())

if n == 0 :
    print(0)
else:
    cards = list(map(int, input().split()))
    dp = [0] * (n+1)

    for i in range(1, n + 1):
        dp[i] = cards[i-1]
        for j in range(1, i + 1):
            dp[i] = max(dp[i], dp[i - j] + cards[j - 1])

    print(dp[n])