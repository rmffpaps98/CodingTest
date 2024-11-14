import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n = int(input())


def draw(n):
    if n == 3:
        return ["***", "* *", "***"]

    star = draw(n // 3)
    result = []

    for i in star:
        result.append(i * 3)
    for i in star:
        result.append(i + ' ' * (n // 3) + i)
    for i in star:
        result.append(i * 3)

    return result


print('\n'.join(draw(n)))