import sys
input = sys.stdin.readline

n = int(input())
p = []
m = []
answer = 0

for _ in range(n):
    num = int(input())
    if num > 1:
        p.append(num)
    elif num <= 0:
        m.append(num)
    else:
        answer += 1

p.sort(reverse=True)
m.sort()

for i in range(0, len(p), 2):
    if i + 1 < len(p):
        answer += p[i] * p[i + 1]
    else:
        answer += p[i]

for i in range(0, len(m), 2):
    if i + 1 < len(m):
        answer += m[i] * m[i + 1]
    else:
        answer += m[i]

print(answer)