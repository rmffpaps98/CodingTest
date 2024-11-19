import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())

remaining = n + m - k

print(min(n // 2, m, remaining // 3))