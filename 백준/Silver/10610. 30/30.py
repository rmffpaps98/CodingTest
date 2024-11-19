import sys
input = sys.stdin.readline

n = list(map(str, input().strip()))
n_sum = 0
has_zero = False

for i in n:
    n_sum += int(i)
    if i == '0':
        has_zero = True

if not has_zero or n_sum % 3 != 0:
    print(-1)
else:
    print(''.join(sorted(n, reverse=True)))