import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

v = int(input())
tree = [[] for _ in range(v+1)]

for _ in range(v):
    line = list(map(int, input().split()))
    node = line[0]
    idx = 1
    while line[idx] != -1:
        n_num, n_dis = line[idx], line[idx+1]
        tree[node].append((n_num, n_dis))
        idx += 2

visited = [-1] * (v+1)
visited[1] = 0


def dfs(node, dis):
    for v, d in tree[node]:
        distance = dis + d
        if visited[v] == -1:
            visited[v] = distance
            dfs(v, distance)


dfs(1, 0)
tmp = [0, 0]

for i in range(1, len(visited)):
    if visited[i] > tmp[1]:
        tmp[1] = visited[i]
        tmp[0] = i

visited = [-1] * (v+1)
visited[tmp[0]] = 0
dfs(tmp[0], 0)

print(max(visited))