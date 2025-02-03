import sys
input = sys.stdin.readline

n, m = map(int, input().split())
wd = {}

for _ in range(n):
    word = input().strip()
    if len(word) >= m:
        wd[word] = wd.get(word, 0) + 1

wd = sorted(wd.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

for word, _ in wd:
    print(word)