import sys
from collections import deque
input = sys.stdin.readline


def dfs(graph, visited, v):
    visited[v] = True
    print(v, end=' ')
    for i in sorted(graph[v]):
        if not visited[i]:
            dfs(graph, visited, i)


def bfs(graph, v):
    queue = deque([v])
    visited = [False] * (len(graph) + 1)

    while queue:
        V = queue.popleft()
        if not visited[V]:
            visited[V] = True
            print(V, end=' ')
            for i in sorted(graph[V]):
                if not visited[i]:
                    queue.append(i)


n, m, v = map(int, input().split())
visited = [False] * (n+1)
graph = [[] for _ in range(n+1)]
for _ in range(m):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)

dfs(graph, visited, v)
print()
bfs(graph, v)