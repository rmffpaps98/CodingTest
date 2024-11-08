from collections import deque
import sys
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs():
    queue = deque([(0, 0)])
    distance[0][0] = 1

    while queue:
        x, y = queue.popleft()

        if x == n - 1 and y == m - 1:
            return distance[x][y]

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] == 1 and distance[nx][ny] == 0:
                distance[nx][ny] = distance[x][y] + 1
                queue.append((nx, ny))
    return -1

n, m = map(int, input().split())
maze = [list(map(int, input().strip())) for _ in range(n)]
distance = [[0] * m for _ in range(n)]

result = bfs()
print(result)