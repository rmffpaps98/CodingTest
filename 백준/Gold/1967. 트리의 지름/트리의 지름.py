import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
tree = [[] for _ in range(n+1)]

for _ in range(n-1):
    p, c, d = list(map(int, input().split()))
    tree[p].append((c, d))
    tree[c].append((p, d))

def dfs(start, d):
    for node, dis in tree[start]:
        if visited[node] == -1:
            visited[node] = d + dis
            dfs(node, visited[node])

visited = [-1] * (n+1)
visited[1] = 0
dfs(1, 0)

last = visited.index(max(visited))
visited = [-1] * (n+1)
visited[last] = 0
dfs(last, 0)

print(max(visited))