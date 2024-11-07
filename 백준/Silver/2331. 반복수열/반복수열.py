import sys

sys.setrecursionlimit(10 ** 6)


def next_number(x, p):
    return sum(int(i) ** p for i in str(x))


def dfs(sequence, v, visited):
    visited[v] = len(sequence)
    sequence.append(v)
    next_v = next_number(v, p)

    if next_v in visited:
        return len(sequence[:visited[next_v]])
    else:
        return dfs(sequence, next_v, visited)


a, p = map(int, input().split())
visited = {}
answer = dfs([], a, visited)
print(answer)