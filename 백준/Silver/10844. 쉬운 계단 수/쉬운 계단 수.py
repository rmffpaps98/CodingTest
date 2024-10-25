N = int(input())

previous_dp = [0] * 10
current_dp = [0] * 10

for i in range(1, 10):
    previous_dp[i] = 1

for i in range(2, N + 1):
    current_dp[0] = previous_dp[1]
    current_dp[9] = previous_dp[8]

    for j in range(1, 9):
        current_dp[j] = (previous_dp[j - 1] + previous_dp[j + 1])

    previous_dp, current_dp = current_dp, previous_dp

print(sum(previous_dp) % 1000000000)