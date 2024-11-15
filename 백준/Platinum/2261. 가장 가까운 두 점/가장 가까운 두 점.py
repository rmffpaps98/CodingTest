import sys
input = sys.stdin.readline

n = int(input())
p = []
for _ in range(n):
    x, y = map(int, input().split())
    p.append((x, y))

p.sort()


def distance_squared(p1, p2):
    return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2


def closest_pair(start, end):
    if end - start + 1 <= 3:
        min_dist = float('inf')
        for i in range(start, end):
            for j in range(i + 1, end + 1):
                min_dist = min(min_dist, distance_squared(p[i], p[j]))
        return min_dist

    mid = (start + end) // 2
    mid_x = p[mid][0]

    min_left = closest_pair(start, mid)
    min_right = closest_pair(mid + 1, end)
    min_dist = min(min_left, min_right)

    tmp = []
    for i in range(start, end + 1):
        if (p[i][0] - mid_x) ** 2 < min_dist:
            tmp.append(p[i])

    tmp.sort(key=lambda point: point[1])

    t = len(tmp)
    for i in range(t - 1):
        for j in range(i + 1, t):
            if (tmp[j][1] - tmp[i][1]) ** 2 >= min_dist:
                break
            min_dist = min(min_dist, distance_squared(tmp[i], tmp[j]))

    return min_dist


min_distance_squared = closest_pair(0, n - 1)

print(min_distance_squared)