import sys
input = sys.stdin.readline

n = int(input())

# def fib(n):
#     if n == 1 or n == 2:
#         return 1
#     return fib(n-1) + fib(n-2)
#
# print(fib(n))

dp = [0] * 91
dp[1] = 1
dp[2] = 1

for i in range(3, n+1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[n])