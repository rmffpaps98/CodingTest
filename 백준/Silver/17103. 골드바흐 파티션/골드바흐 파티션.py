import sys
input = sys.stdin.readline


def sieve(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return is_prime


n = int(input())
q = [int(input()) for _ in range(n)]
max_val = max(q)

prime_list = sieve(max_val)

for i in q:
    cnt = 0
    for j in range(2, i // 2 + 1):
        if prime_list[j] and prime_list[i - j]:
            cnt += 1
    print(cnt)