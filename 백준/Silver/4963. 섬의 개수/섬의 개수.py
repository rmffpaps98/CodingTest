import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

dx = [1, 1, -1, -1, 1, -1, 0, 0]
dy = [0, 1, 0, -1, -1, 1, 1, -1]


def dfs(x, y):
    maps[x][y] = 0
    for i in range(8):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < h and 0 <= ny < w and maps[nx][ny] == 1:
            dfs(nx, ny)


while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    maps = [list(map(int, input().split())) for _ in range(h)]
    cnt = 0

    for i in range(h):
        for j in range(w):
            if maps[i][j] == 1:
                dfs(i, j)
                cnt += 1

    print(cnt)