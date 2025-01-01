m = int(input())
n = int(input())

def is_prime(n):
    if n == 1:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

s = 0
min_num = 0
for i in range(m, n+1):
    if is_prime(i):
        s += i
        if min_num == 0:
            min_num = i

if s != 0:
    print(s)
    print(min_num)
else:
    print(-1)