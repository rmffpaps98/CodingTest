import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def dfs(graph, v, visited):
    visited[v] = True

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i ,visited)

t = int(input())

for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    graph = [[] for _ in range(n+1)]
    visited = [False] * (n+1)
    cnt = 0

    for idx, i in enumerate(nums):
        graph[idx+1].append(i)
        graph[i].append(idx+1)

    for i in range(1, n+1):
        if not visited[i]:
            dfs(graph, i, visited)
            cnt += 1

    print(cnt)