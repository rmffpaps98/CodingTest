from collections import deque
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
land = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    land[x][y] = mark

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if land[nx][ny] == 1:
                    q.append((nx, ny))
                    land[nx][ny] = mark
                    visited[nx][ny] = True


def bfs2(num):
    q = deque()
    dist = [[-1] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if land[i][j] == num:
                q.append((i, j))
                dist[i][j] = 0

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if land[nx][ny] != num and land[nx][ny] != 0:
                    return dist[x][y]
                if land[nx][ny] == 0 and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))


mark = 1
for x in range(n):
    for y in range(n):
        if land[x][y] == 1 and not visited[x][y]:
            cnt = bfs(x, y)
            mark += 1

answer = sys.maxsize
for i in range(1, mark):
    answer = min(answer, bfs2(i))

print(answer)