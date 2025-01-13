import sys
input = sys.stdin.readline


def sieve(max_num):
    is_prime = [True] * (max_num + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(max_num ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, max_num + 1, i):
                is_prime[j] = False
    return is_prime


MAX_LIMIT = 123456 * 2
prime_list = sieve(MAX_LIMIT)

while True:
    n = int(input())
    if n == 0:
        break

    cnt = sum(prime_list[n + 1:(2 * n) + 1])
    print(cnt)