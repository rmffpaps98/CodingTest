import sys
input = sys.stdin.readline

n = int(input())  
words = set()
cnt = 0

for _ in range(n):
    e = input().strip()
    if e == "ENTER":
        cnt += len(words)
        words.clear()
    else:
        words.add(e)

print(cnt + len(words))
