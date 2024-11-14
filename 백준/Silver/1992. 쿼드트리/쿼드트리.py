import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
vid = [list(map(int, input().strip())) for _ in range(n)]


def quad(n, v):
    total_sum = sum(sum(row) for row in v)

    if total_sum == n**2:
        return '1'
    if total_sum == 0:
        return '0'

    tmp = ''
    half = n // 2
    tmp += '('
    tmp += quad(half, [row[:half] for row in v[:half]])
    tmp += quad(half, [row[half:] for row in v[:half]])
    tmp += quad(half, [row[:half] for row in v[half:]])
    tmp += quad(half, [row[half:] for row in v[half:]])
    tmp += ')'

    return tmp


print(quad(n, vid))