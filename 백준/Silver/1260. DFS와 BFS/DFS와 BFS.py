from collections import deque

N, M, V = map(int, input().split())

graph = [[0] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

v1 = [0] * (N+1)
v2 = [0] * (N+1)

def bfs(V):
    q = deque([V])
    v2[V] = True
    while q:
        V = q.popleft()
        print(V, end=" ")
        for i in range(1, N + 1):
            if not v2[i] and graph[V][i]:
                q.append(i)
                v2[i] = True

def dfs(V):
    v1[V] = 1
    print(V, end=" ")
    for i in range(1, N+1):
        if not v1[i] and graph[V][i]:
            dfs(i)

dfs(V)
print()
bfs(V)