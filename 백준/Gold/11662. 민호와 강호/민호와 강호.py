import sys
import math
input = sys.stdin.readline

ax, ay, bx, by, cx, cy, dx, dy = map(int, input().split())

def distance(t):
    mx = ax + (bx - ax) * t
    my = ay + (by - ay) * t

    kx = cx + (dx - cx) * t
    ky = cy + (dy - cy) * t

    return math.sqrt((mx - kx)** 2 + (my - ky) ** 2)

left, right = 0.0, 1.0
for _ in range(100):
    mid1 = (2 * left + right) / 3
    mid2 = (left + 2 * right) / 3

    dist1 = distance(mid1)
    dist2 = distance(mid2)

    if dist1 < dist2:
        right = mid2
    else:
        left = mid1

print(f"{distance((left + right) / 2):.10f}")