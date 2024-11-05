a, b = map(int, input().split())
m = int(input())
digits = list(map(int, input().split()))

val = 0
for i in range(m):
    val = val * a + digits[i]

answer = []
while val > 0:
    val, mod = divmod(val, b)
    answer.append(str(mod))

print(" ".join(answer[::-1]))