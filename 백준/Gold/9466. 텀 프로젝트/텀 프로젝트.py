import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(v, selected, visited):
    stack = []
    while True:
        if visited[v] == 1:
            if v in stack:
                return len(stack[stack.index(v):])
            return 0
        elif visited[v] == 2:
            return 0

        visited[v] = 1
        stack.append(v)
        v = selected[v]

    for node in stack:
        visited[node] = 2

t = int(input())
answer = []

for _ in range(t):
    n = int(input())
    selected = [0] + list(map(int, input().split()))
    visited = [0] * (n + 1)
    team_members = 0

    for i in range(1, n + 1):
        if visited[i] == 0:
            team_members += dfs(i, selected, visited)

    answer.append(n - team_members)

print("\n".join(map(str, answer)))