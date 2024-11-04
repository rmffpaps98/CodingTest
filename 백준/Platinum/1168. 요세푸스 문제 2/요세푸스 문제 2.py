# 혼자 해결 불가

import sys
input = sys.stdin.readline


def init(node, start, end):
    if start == end:
        tree[node] = 1
        return

    mid = (start + end) // 2
    init(2 * node, start, mid)
    init(2 * node + 1, mid + 1, end)
    tree[node] = tree[2 * node] + tree[2 * node + 1]


def query(node, start, end, order):
    if tree[node] == 0:
        return -1
    tree[node] -= 1
    if start == end:
        return start
    mid = (start + end) // 2
    if tree[2 * node] >= order:
        return query(2 * node, start, mid, order)

    return query(2 * node + 1, mid + 1, end, order - tree[2 * node])


n, k = map(int, input().split())
if n == 0:
    print("<>")
    sys.exit()

tree = [0] * (4 * n)
order = k
init(1, 1, n)

print("<", end="")
for _ in range(1, n):
    idx = query(1, 1, n, order)
    if idx == -1:
        break
    print(idx, end=", ")
    order += k - 1
    order = (order - 1) % tree[1] + 1

idx = query(1, 1, n, order)
if idx != -1:
    print(idx, end="")
print(">")