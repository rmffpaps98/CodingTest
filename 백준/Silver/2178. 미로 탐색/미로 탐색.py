import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def bfs():
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    queue = deque([(0, 0)])
    dist[0][0] = 1

    while queue:
        x, y = queue.popleft()

        if x == n-1 and y == m-1:
            return dist[x][y]

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]

            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1 and dist[nx][ny] == 0:
                dist[nx][ny] = dist[x][y] + 1
                queue.append((nx, ny))

n, m = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(n)]
dist = [[0] * m for _ in range(n)]

print(bfs())