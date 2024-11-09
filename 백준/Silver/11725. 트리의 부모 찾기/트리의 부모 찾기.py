import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
tree = [[] for _ in range(n+1)]
parent = [0] * (n+1)

for _ in range(1, n):
    i, j = map(int, input().split())
    tree[i].append(j)
    tree[j].append(i)
    

def dfs(node):
    for i in tree[node]:
        if parent[i] == 0:
            parent[i] = node
            dfs(i)


dfs(1)

for i in range(2, n+1):
    print(parent[i])