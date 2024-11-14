import sys
input = sys.stdin.readline

n = int(input().strip())
stars = [[' ' for _ in range(2 * n)] for _ in range(n)]


def draw_triangle(x, y, size):
    if size == 3:
        stars[x][y] = '*'
        stars[x + 1][y - 1] = stars[x + 1][y + 1] = '*'
        for i in range(-2, 3):
            stars[x + 2][y + i] = '*'
    else:
        half = size // 2
        draw_triangle(x, y, half)
        draw_triangle(x + half, y - half, half)
        draw_triangle(x + half, y + half, half)


draw_triangle(0, n - 1, n)

for row in stars:
    print("".join(row))