import sys
input = sys.stdin.readline

n = int(input())

def draw(n):
    if n == 3:
        return ["***", "* *", "***"]

    star = draw(n//3)
    list = []

    for i in star:
        list.append(i * 3)
    for i in star:
        list.append(i + ' ' * (n // 3) + i)
    for i in star:
        list.append(i * 3)

    return list

print('\n'.join(draw(n)))