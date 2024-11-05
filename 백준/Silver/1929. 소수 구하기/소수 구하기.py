def is_prime(n):
    if n == 1:
        return False

    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

n, m = map(int, input().split())
nums = list(range(n, m+1))
cnt = 0

for i in nums:
    if is_prime(i):
        print(i)