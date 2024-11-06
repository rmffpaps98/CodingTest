def dfs(graph, v, visited):
    visited[v] = 1
    result = [v]
    for i in sorted(graph[v]):
        if not visited[i]:
            result.extend(dfs(graph, i, visited))
    return result

def bfs(graph, start, visited):
    queue = [start]
    visited[start] = 1
    result = [start]
    while queue:
        v = queue.pop(0)
        for i in sorted(graph[v]):
            if not visited[i]:
                queue.append(i)
                visited[i] = 1
                result.append(i)
    return result

n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)

visited = [0] * (n + 1)
print(' '.join(map(str, dfs(graph, v, visited))))

visited = [0] * (n + 1)
print(' '.join(map(str, bfs(graph, v, visited))))