import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


def iterative_dfs(start, group):
    stack = [(start, group)]
    visited[start] = group

    while stack:
        node, group = stack.pop()

        for i in graph[node]:
            if visited[i] == 0:
                visited[i] = -group
                stack.append((i, -group))
            elif visited[i] == group:
                return False
    return True


k = int(input())

for _ in range(k):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v + 1)]
    visited = [0] * (v + 1)

    for _ in range(e):
        i, j = map(int, input().split())
        graph[i].append(j)
        graph[j].append(i)

    result = True
    for i in range(1, v + 1):
        if visited[i] == 0:
            if not iterative_dfs(i, 1):
                result = False
                break

    print('YES' if result else 'NO')