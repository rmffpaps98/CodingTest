n = int(input())
f = 1

# n! 계산
for i in range(n, 0, -1):
    f *= i

for idx, i in enumerate(str(f)[::-1]):
    if i != '0':
        print(idx)
        break