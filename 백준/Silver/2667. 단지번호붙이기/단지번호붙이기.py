import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return 0

    if graph[x][y] == 1:
        graph[x][y] = 0
        count = 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            count += dfs(nx, ny)

        return count
    return 0


n = int(input())
graph = [list(map(int, input().strip())) for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

num = []
answer = 0

for i in range(n):
    for j in range(n):
        group_size = dfs(i, j)
        if group_size > 0:
            num.append(group_size)
            answer += 1

num.sort()
print(answer)
for size in num:
    print(size)