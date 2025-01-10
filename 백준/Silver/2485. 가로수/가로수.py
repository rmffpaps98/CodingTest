import sys
input = sys.stdin.readline


def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


n = int(input())
col = []
d = []

for i in range(n):
    col.append(int(input()))

    if i != 0:
        d.append(col[i] - col[i - 1])

mg = d[0]
for i in range(1, len(d)):
    mg = gcd(mg, d[i])

total_trees = (col[-1] - col[0]) // mg + 1
result = total_trees - n
print(result)