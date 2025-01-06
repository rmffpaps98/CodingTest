n, m = map(int, input().split())
board = [input().strip() for _ in range(n)]

chess_white_start = [
    ['W', 'B'] * 4,
    ['B', 'W'] * 4
] * 4

chess_black_start = [
    ['B', 'W'] * 4,
    ['W', 'B'] * 4
] * 4


def count_repaints(x, y):
    count_white_start = 0
    count_black_start = 0
    for i in range(8):
        for j in range(8):
            if board[x + i][y + j] != chess_white_start[i][j]:
                count_white_start += 1
            if board[x + i][y + j] != chess_black_start[i][j]:
                count_black_start += 1

    return min(count_white_start, count_black_start)

min_repaints = float('inf')
for i in range(n - 7):
    for j in range(m - 7):
        min_repaints = min(min_repaints, count_repaints(i, j))

print(min_repaints)