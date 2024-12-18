import sys
input = sys.stdin.readline

def dfs(graph, v, visited):
    visited[v] = True

    for i in sorted(graph[v]):
        if not visited[i]:
            dfs(graph, i, visited)


n = int(input())
com = int(input())
visited = [False] * (n+1)
graph = [[] for _ in range(n+1)]
for _ in range(com):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)


dfs(graph, 1, visited)
print(len([i for i in visited if i])-1)